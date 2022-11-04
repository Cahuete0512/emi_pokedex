from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Site en construction")

def hello(request):
    text = "<h1> Bienvenu sur le Pokedex d'EMI ! <h1><p><p>"
    return HttpResponse

def result(request, number):
    text = "Le resultat de la requete %d." %number
    return HttpResponse(text)




