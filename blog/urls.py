"""URL permettant une meilleure modularilte de l'application lors de la migration"""
from django.urls import path
from . import views

urlpatterns = [
    path('acceuil', views.home),
    path('article/<int:id_article>', views.view_article),
    path('articles/<int:month>/<int:year>', views.list_articles),
    path('date', views.date),
    path('addition/<int:n1>/<int:n2>', views.addition)
]