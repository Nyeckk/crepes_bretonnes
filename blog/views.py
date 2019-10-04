from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """A function that return an http response of ourselve"""
    return HttpResponse("""
            <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p
        """)
