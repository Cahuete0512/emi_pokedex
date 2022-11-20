from django.shortcuts import render
from django.http import HttpResponse, request


def index(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './index.html', context)


def hello(request):
    text = "<h1> Bienvenu sur le Pokedex d'EMI ! <h1><p><p>"
    return HttpResponse(text)


def result(request, number):
    text = "Le resultat de la requete %d." % number
    return HttpResponse(text)


def naviguerEntrePokemon(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './naviguerEntrePokemon.html', context)


def equipe(request):
    context = {
        'name': 'John Doe',
        'pokemonsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe.html', context)


