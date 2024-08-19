from django.contrib import admin
from .models import Article
from .models import Testimonial
from django.contrib.admin import AdminSite


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_date', 'author')
    list_filter = ('category',)
    search_fields = ('title', 'content')
    ordering = ('-published_date',)  # Articles les plus récents en premier

admin.site.register(Article, ArticleAdmin)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author', 'content')  # Affiche les champs dans la liste d'administration
    search_fields = ('author', 'content')  # Permet de rechercher par auteur ou contenu

# Personnaliser le titre de la page d'administration
admin.site.site_header = "Tableau de Bord AddictedPress"
admin.site.site_title = "Administration AddictedPress"
admin.site.index_title = "Bienvenue sur l'administration d'AddictedPress"

