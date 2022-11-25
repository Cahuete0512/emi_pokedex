import requests
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

            id = str(i['url'][42])
            if i['url'][43] != "/":
                id = id + str(i['url'][43])
            tab.append(id)

            #     je refais un appel avec l'id
            r2 = requests.get('https://pokeapi.co/api/v2/pokemon/' + id + '/')
            if r2.status_code == 200:
                result3 = r2.json()
                pokemon = Pokemon()
                pokemon.speciesName = result3['species']['name']
                pokemon.picture = result3['sprites']['front_default']
                pokemon.types = "test"
                pokemon.abilities = "abilities"
                pokemon.weight = "20"
                pokemon.save()
                resultPokemon.append(pokemon)

        context = {
            'pokemonList': resultPokemon
        }
        return render(request, './pokemonPage.html', context)
    return HttpResponse('Could not save data')


def naviguer_entre_pokemon(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './naviguer_entre_pokemon.html', context)


def equipe(request):
    context = {
        'name': 'John Doe',
        'pokemonsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1']
    }
    return render(request, './cartesEquipe.html', context)
