"""
URL configuration for Journal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Journal.views import admin_dashboard, login, register, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'administration Django
    path('journal/', include('Journal.urls')),  # URL pour l'application Journal
    path('', include('Journal.urls')),  # URL pour la racine (page d'accueil)
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),  # URL pour le tableau de bord
    path('login/', login, name='login'),  # URL pour la connexion
    path('admin/logout/', custom_logout, name='admin_logout'),  # URL pour la déconnexion
    path('register/', register, name='register'),  # URL pour l'inscription
]
# Ajouter la configuration pour les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


