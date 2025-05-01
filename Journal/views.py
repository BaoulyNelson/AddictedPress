# views.py
from django.shortcuts import render, get_object_or_404
from .models import Article,Testimonial
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TestimonialForm,ProfileForm ,ContactForm # Assurez-vous d'utiliser le bon formulaire
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.contrib import messages
from django.contrib.messages import get_messages
from Journal.utils import ajouter_message




@login_required
def profile(request):
    return render(request, 'comptes/profile.html', {'user': request.user})



def login_view(request):
    # Supprime les anciens messages avant d'afficher un nouveau
    storage = get_messages(request)
    for _ in storage:
        pass  # Cette boucle vide supprime tous les anciens messages

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue {username} ! 😊 Vous êtes connecté.")

                if request.POST.get("remember_me"):
                    request.session.set_expiry(1209600)  # 2 semaines

                return redirect("user_profile")
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(request, "Veuillez vérifier vos informations.")
    else:
        form = AuthenticationForm()

    return render(request, "comptes/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! 🎉 Bienvenue sur notre plateforme.")
            return redirect("index")  # Redirection après succès
        else:
            messages.error(request, "Une erreur est survenue lors de l'inscription. Vérifiez les informations.")
    else:
        form = UserCreationForm()

    return render(request, "comptes/signup.html", {"form": form})



@login_required
def confirmer_deconnexion(request):
    if request.method == 'POST':
        logout(request)
        ajouter_message(request, 'success', "Vous vous êtes déconnecté avec succès.")
        return redirect('index')
    return render(request, 'comptes/confirmer_deconnexion.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige vers la page d'accueil ou une autre page après la mise à jour
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'comptes/edit_profile.html', {'form': form})



def index(request):
    actualites_articles = Article.objects.filter(category='actualites').order_by('-published_date')
    
    all_articles_list = Article.objects.exclude(category__in=['actualites']).order_by('-published_date')
    print(f"Nombre d'articles paginés : {all_articles_list.count()}")  # Vérification

    paginator = Paginator(all_articles_list, 5)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    context = {
        'actualites_articles': actualites_articles,
        'articles': articles,
    }
    
    return render(request, 'index.html', context)



def about(request):
    return render(request, 'about.html')



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # 📩 Envoyer un email (optionnel)
            send_mail(
                f"Nouveau message de {name}",
                message,
                email,
                ["admin@example.com"],  # Remplace avec l'email de ton admin
                fail_silently=False,
            )

            return redirect("contact_success")  # Redirige vers une page de succès
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})


def contact_success_view(request):
    return render(request, "contact/contact_success.html")


def testimonials(request):
    return render(request, 'commentaires/testimonials.html')


def articles_by_category(request, category_name):
    # Récupération des articles de la catégorie
    articles_list = Article.objects.filter(category=category_name).order_by('-published_date')

    # Pagination (5 articles par page)
    paginator = Paginator(articles_list, 5)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)

    # Contexte envoyé au template
    context = {
        'articles': articles,
        'category': category_name
    }

    return render(request, 'articles/articles_by_category.html', context)



def article_detail(request, id):  # Modifier article_id → id
    article = get_object_or_404(Article, id=id)

    # Récupérer les articles recommandés
    recommended_articles = Article.objects.filter(category=article.category).exclude(id=article.id).order_by('-published_date')[:5]

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'recommended_articles': recommended_articles
    })



def search(request):
    query = request.GET.get('q', '')

    # Rechercher dans les articles
    articles = Article.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(category__icontains=query)
    ).order_by('-published_date')

    # Rechercher dans les témoignages
    testimonials = Testimonial.objects.filter(
        Q(content__icontains=query)  # Pas de tri par date, car il n'existe pas de champ date
    )

    context = {
        'articles': articles,
        'testimonials': testimonials,
        'query': query
    }
    return render(request, 'search/search_results.html', context)





def testimonials(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    
    testimonials = Testimonial.objects.all()
    return render(request, 'commentaires/testimonials.html', {'testimonials': testimonials, 'form': form})





