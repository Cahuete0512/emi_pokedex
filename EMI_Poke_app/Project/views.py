import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import EquipeForm
from .models import Pokemon
from .models import Equipe


def index(request):
    pokemons = Pokemon.objects.all()
    if not pokemons:
        r = requests.get('https://pokeapi.co/api/v2/generation/1')
        if r.status_code == 200:
            result = r.json()
            tab_id_pokemon = []
            tab_pokemon = []
            for i in result['pokemon_species']:

                id = str(i['url'][42])
                if i['url'][43] != "/":
                    id = id + str(i['url'][43])
                tab_id_pokemon.append(id)

                # 2ème appel pour récuperer les informations de chaque pokemon grace à leur id
                r2 = requests.get('https://pokeapi.co/api/v2/pokemon/' + id + '/')
                if r2.status_code == 200:

                    result_pokemon = r2.json()

                    pokemon = Pokemon()
                    pokemon.speciesName = result_pokemon['species']['name']
                    pokemon.picture = result_pokemon['sprites']['front_default']

                    # Récupération des noms des types des pokemons
                    types = ""
                    for element in result_pokemon['types']:
                        types = str(element["type"]["name"]) + " " + types
                    pokemon.types = types

                    # Récupération des noms des abilités des pokemons
                    abilities = ""
                    for element in result_pokemon['abilities']:
                        abilities = str(element["ability"]["name"]) + " " + abilities
                    pokemon.abilities = abilities

                    pokemon.weight = result_pokemon['weight']
                    pokemon.save()

                    tab_pokemon.append(pokemon)

            context = {
                'pokemonList': tab_pokemon
            }
    else:
        context = {
            'pokemons': pokemons
        }
    return render(request, './index.html', context)


def naviguer_entre_pokemon(request):
    pokemons = Pokemon.objects.all()
    context = {
        'pokemons': pokemons
    }
    return render(request, './naviguer_entre_pokemon.html', context)


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
    return render(request, './cartes_equipe.html', context)


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
    return render(request, './equipe_details.html', context)


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
