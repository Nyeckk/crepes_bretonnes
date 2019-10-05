"""URL permettant une meilleure modularilte de l'application lors de la migration"""
from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.home),
    path('article/<int:id_article>', views.view_article),
    path('articles/<int:month>/<int:year>', views.list_articles)
]