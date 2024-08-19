# models.py
from django.db import models
from django.contrib.auth.models import User  # Pour l'auteur

# Liste des choix de catégories
CATEGORIE_CHOICES = [
    ('actualites', 'Actualités'),
    ('annonces', 'Annonces'),
    ('culture', 'Culture'),
    ('economie', 'Économie'),
    ('sport', 'Sport'),
    ('editorial', 'Éditorial'),
    ('national', 'National'),
    ('opinions', 'Opinions'),
    ('societe', 'Société'),
]

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-published_date']  # Articles les plus récents en premier

    def __str__(self):
        return self.title



class Testimonial(models.Model):
    author = models.CharField(max_length=100)  # Nom ou pseudonyme de l'auteur du témoignage
    content = models.TextField()                # Contenu du témoignage

    def __str__(self):
        return self.author
