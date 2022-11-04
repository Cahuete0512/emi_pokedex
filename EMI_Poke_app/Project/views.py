from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'name' : 'John Doe',
        'weaponsList' : ['Epée', 'Bouclier', 'Petite cuillère']
    }
    return render(request, './index.html', context)

def hello(request):
    text = "<h1> Bienvenu sur le Pokedex d'EMI ! <h1><p><p>"
    return HttpResponse(text)

def result(request, number):
    text = "Le resultat de la requete %d." %number
    return HttpResponse(text)




