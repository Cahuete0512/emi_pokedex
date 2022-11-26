import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import EquipeForm
from .models import Pokemon
from .models import Equipe


def index(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons': pokemons
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
        tabId = []
        tabPokemon = []
        for i in result['pokemon_species']:

            id = str(i['url'][42])
            if i['url'][43] != "/":
                id = id + str(i['url'][43])
            tabId.append(id)

            # 2ème appel pour récuperer les informations de chaque pokemon grace à leur id
            r2 = requests.get('https://pokeapi.co/api/v2/pokemon/' + id + '/')
            if r2.status_code == 200:

                resultPokemon = r2.json()

                pokemon = Pokemon()
                pokemon.speciesName = resultPokemon['species']['name']
                pokemon.picture = resultPokemon['sprites']['front_default']

                # Récupération des noms des types des pokemons
                types = ""
                for element in resultPokemon['types']:
                    types = str(element["type"]["name"]) + " " + types
                pokemon.types = types

                # Récupération des noms des abilités des pokemons
                abilities = ""
                for element in resultPokemon['abilities']:
                    abilities = str(element["ability"]["name"]) + " " + abilities
                pokemon.abilities = abilities

                pokemon.weight = resultPokemon['weight']
                pokemon.save()

                tabPokemon.append(pokemon)

        context = {
            'pokemonList': tabPokemon
        }
        return render(request, './pokemonPage.html', context)
    return HttpResponse('Could not save data')


def naviguer_entre_pokemon(request):
    context = {
        'name': 'John Doe',
        'weaponsList': ['Epée', 'Bouclier', 'Petite cuillère', 'Test 1', 'Test 1', 'Test 1', 'Test 1']
    }
    return render(request, './naviguerEntrePokemon.html', context)


def equipe(request):
    equipes = Equipe.objects.all()
    if not equipes:
        context = {
            'equipe': 0,
        }
    else:
        context = {
            'equipe': 1,
            'equipeList': equipes
        }
    return render(request, './cartesEquipe.html', context)


def equipe_details(request, id):
    equipe = Equipe.objects.get(id=id)
    if not equipe:
        context = {
            'equipeExist': 0,
            'equipeId': id
        }
    else:
        context = {
            'equipeExist': 1,
            'equipe': equipe,
            'equipeId': id,
        }
    return render(request, './equipeDetails.html', context)


def create_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('list_equipes')
    else:
        form = EquipeForm()
    return render(request, './create_equipe.html', {'form': form})


def update_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    form = EquipeForm(request.POST, instance=equipe)
    if form.is_valid():
        form.save()
        return redirect('list_equipes')

    else:
        form = EquipeForm(instance=equipe)

    context = {
        'form': form,
        'equipe': equipe,
    }
    return render(request, 'update_equipe.html', context)


def delete_equipe(request, id):
    equipe = Equipe.objects.get(id=id)
    equipe.delete()
    return redirect('index')
