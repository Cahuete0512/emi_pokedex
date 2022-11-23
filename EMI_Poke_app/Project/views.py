from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

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

def api_call(request):
    r = requests.get('https://pokeapi.co/api/v2/generation/1')
    if r.status_code == 200:
        result = r.json()
        tab = []
        resultPokemon = []
        pokemonImage = []
        for i in result['pokemon_species']:
            pokemon = []
            id = str(i['url'][42])
            if i['url'][43] != "/":
                id = id + str(i['url'][43])
            tab.append(id)

        #     je refais un appel avec l'id
            r2 = requests.get('https://pokeapi.co/api/v2/pokemon/' + id + '/')
            if r2.status_code == 200:
                result3 = r2.json()
                Pokemon.__name__=result3['species']['name']
                pokemon.append(result3['species']['name'])
                pokemon.append(result3['sprites']['front_default'])
                resultPokemon['name'].append(pokemon)


        context = {
            'pokemonList' : resultPokemon,
             'pokemonImage' : pokemonImage
        }
        return render(request, './pokemonPage.html', context)
    return HttpResponse('Could not save data')



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


