from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    """
    Classe representant un article.
    """

    titre = models.CharField(max_length=50)
    auteur = models.CharField(max_length=100)
    contenu = models.TextField(null=True)
    date_parution = models.DateTimeField(default=timezone.now, verbose_name='date de parution')

    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class meta:
        verbose_name = 'article'
        ordering = ['date_parution']

    def __str__(self):
        return self.titre


class Categorie(models.Model):
    """
    Classe represantant les differentes categories
    """

    nom = models.CharField(max_length=30)
    
    class meta():
        verbose_name = 'categorie'
        ordering = ['nom']
    
    def __str__(self):
        return self.nom