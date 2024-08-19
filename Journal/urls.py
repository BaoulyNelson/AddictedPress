from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    # Route pour la page d'accueil
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # À propos
    path('contact/', views.contact, name='contact'),  # Contact
    path('testimonials/', views.testimonials, name='testimonials'),  # Témoignages
   

    # Route pour les articles par catégorie
    path('category/<str:category_name>/', views.articles_by_category, name='articles_by_category'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),  # Ajouter cette ligne
    path('search_by_category/', views.search_by_category, name='search_by_category'),
    path('explore/', views.all_articles, name='all_articles'),
  
  
]
