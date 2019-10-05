from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime

# Create your views here.

def home(request):
    """A function that return an http response of ourselve"""
    return HttpResponse("""
            <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p
        """)

def view_article(request, id_article):
    """
    Renvoi un article selon son identifiant passE en parametre,
    ici <id_article> et s'il n'existe pas renvoyer une erreur 404
    """
    if id_article > 100:
        # Si l'id est superieur a 100 on considere qu'il n'existe pas.
        raise Http404

    return HttpResponse('Vous avez demandE l\'article {} !'.format(id_article))

def list_articles(request, month, year):
    """
    Renvoie tous les articles uploades durant le mois <month> de l'annee
    <year>. Pour des tests on va faire une redirection vers une page 
    """
    return redirect('http://python.org')

def date(request):
    """
    renvoie la date du jour
    """
    return render(request, 'blog/date.html', {'date':datetime.now()})

def addition(request, n1, n2):
    """
    Renvoie l'addition de deux nombres n1 et n2
    """
    total = n1 + n2
    
    return render(request, 'blog/addition.html', locals())
