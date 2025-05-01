from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# Importation des vues de Django pour la gestion de l'authentification
from django.contrib.auth import views as auth_views

urlpatterns = [

    # Route pour la page d'accueil
    path('', views.index, name='index'),
    # Ajoute cette ligne dans ton `urls.py`
    path('signup/', views.signup_view, name='signup'),
    # Page de connexion
    path('login/', views.login_view, name='login'),
    
    # Page de déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('confirmer-deconnexion/', views.confirmer_deconnexion, name='confirmer_deconnexion'),
    # Exemple de route pour le profil de l'utilisateur
    path('accounts/profile/', views.profile, name='user_profile'),

    # Changer de mot de passe
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Réinitialisation de mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='comptes/password_reset_form.html'
    ), name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='comptes/password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='comptes/password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='comptes/password_reset_complete.html'
    ), name='password_reset_complete'),

    # Page À propos
    path('about/', views.about, name='about'),
    
    # Page Contact
    path("contact/", views.contact_view, name="contact"),
    # Page Témoignages
    path("contact/success/", views.contact_success_view, name="contact_success"),

    path('testimonials/', views.testimonials, name='testimonials'),
   
    # Route pour afficher les articles d'une catégorie spécifique
    path('category/<str:category_name>/', views.articles_by_category, name='articles_by_category'),
    
    # Détail d'un article spécifique par son ID
    path('article/<int:id>/', views.article_detail, name='article_detail'), 
    
    # Route pour effectuer une recherche par catégorie
    path('search_by_category/', views.search, name='search_by_category'),
  
    # URL pour éditer le profil utilisateur
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # URL pour modifier le profil

]
# Gestion des fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
