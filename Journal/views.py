# views.py
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.db.models import Count

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Testimonial
from .forms import TestimonialForm

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


def search_by_category(request):
    category_name = request.GET.get('category', '')
    articles = Article.objects.filter(category=category_name).order_by('-published_date')
    return render(request, 'search_results.html', {'articles': articles, 'category_name': category_name})



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

    context = {
        'total_articles': total_articles,
        'articles_by_category': articles_by_category,
        'total_testimonials': total_testimonials,
    }
    return render(request, 'admin_dashboard.html', context)




