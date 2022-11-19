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


def equipe_1(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe_1.html', context)


def equipe_2(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe_2.html', context)


def equipe_3(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe_3.html', context)


def equipe_4(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe_4.html', context)


def equipe_5(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe_5.html', context)
