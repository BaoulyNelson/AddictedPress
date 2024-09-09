# views.py
from django.shortcuts import render, get_object_or_404
from .models import Article,Testimonial
from django.db.models import Count
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomUserCreationForm  # Assurez-vous d'utiliser le bon formulaire


from .forms import TestimonialForm
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView




def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def testimonials(request):
    return render(request, 'testimonials.html')


def articles_by_category(request, category_name):
    # Filtrer les articles par catégorie et trier par date de publication (les plus récents en premier)
    articles = Article.objects.filter(category=category_name).order_by('-published_date')
    return render(request, 'articles_by_category.html', {'articles': articles, 'category': category_name})

def article_detail(request, id):
    # Obtenir l'article avec l'ID donné
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})

@login_required  # Assure-toi que seuls les utilisateurs connectés peuvent accéder à cette vue
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')


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
    return render(request, 'search_results.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Vous pouvez traiter ou sauvegarder les données ici, par exemple, les envoyer par email
        subject = f"Message de {name} via le formulaire de contact"
        body = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Envoyer l'email (assurez-vous que les paramètres email sont configurés dans settings.py)
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

        # Rediriger après soumission
        return HttpResponse("Merci de nous avoir contactés. Nous vous répondrons sous peu.")

    return render(request, 'contact.html')

def all_articles(request):
    articles = Article.objects.all()
    return render(request, 'all_articles.html', {'articles': articles})

def testimonials(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials, 'form': form})


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    total_articles = Article.objects.count()
    articles_by_category = Article.objects.values('category').annotate(total=Count('category'))
    total_testimonials = Testimonial.objects.count()
    total_users = User.objects.count()  # Compter le nombre total d'utilisateurs
    users = User.objects.all()  # Obtenir tous les utilisateurs

    context = {
        'total_articles': total_articles,
        'articles_by_category': articles_by_category,
        'total_testimonials': total_testimonials,
        'total_users': total_users,  # Ajouter le nombre total d'utilisateurs au contexte
        'users': users,  # Ajouter la liste des utilisateurs au contexte
    }
    return render(request, 'admin_dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Connecte automatiquement l'utilisateur après l'inscription
            return redirect('admin_dashboard')  # Redirige directement vers le tableau de bord après inscription
    else:
        form = CustomUserCreationForm()
    return render(request, 'admin/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)  # Connecte l'utilisateur
                return redirect('admin_dashboard')  # Redirige vers le tableau de bord après connexion
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')

    return render(request, 'admin/login.html')


def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(reverse('admin:index'))  # Redirection après déconnexion
    return render(request, 'admin/logout.html')
