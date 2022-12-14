## Table of Contents
1. [Introduction](#Introduction)
2. [Maquette](#Maquette)
3. [Technologies](#Technologies)
4. [Installation](#Installation)
5. [Collaboration](#Collaboration)
6. [Execution](#Execution)
***
# Introduction

L’objectif de ce projet est de développer un Pokédex.

_Le Pokédex est un outil qui permet de recenser TOUS les Pokémons du jeu_

***
# Maquette

![Alt text](EMI_Poke_app/Project/Assets/maquettePke.PNG?raw=true "Optional Title")
***
# Technologies

* [Python](https://docs.python.org/3.9/) : Version 3.9.6

* [pip](https://pip.pypa.io/en/stable/index.html) : Version 22.3.1

* [Django](https://docs.djangoproject.com/en/4.1/) : Version 4.1.3

* L'OS est de type **Windows** en version 10
***
# Installation

Le projet a été virtualisé avec un virtualenv. 

* Installer pip pour Python [pip](https://pip.pypa.io/en/stable/index.html) : Version 22.3.1
* Installer Django [Django](https://docs.djangoproject.com/en/4.1/) : Version 4.1.3

Clonez d’abord le référentiel à partir de Github et passez au nouveau répertoire :

>    $ git clone https://github.com/Cahuete0512/emi_pokedex.git
***
# Collaboration

Cette application a été réalisée par :

* **Mlle Eline MALHERBE**, 
* **Mlle Magalie CONTANT**,
* **Mlle Ines BOUCARD**

Toutes les trois sont élèves en classe B3, groupe 2, cursus CDA option fullstack à l'EPSI de Nantes.

***
# Choix

Pour la récupération des données de l'api et leur utilisation, nous avons décidé de créer un premier appel qui collecte les 151 pokemons de première génération.
Puis d'effectuer un second appel pour chaque pokémon pour récuperer leurs informations grâce à leur id envoyé en paramètre.
Ces appels ne s'exécutuent qu'au lancement de l'application et nous permettent ensuite de récuperer toutes les données pour les enregistrer en base de données.
Le premier lancement de l'application prend donc quelques secondes au vu du nombre de données à collecter mais nous permet d'avoir ensuite une application peu gourmande en ressources.

***
# Execution

> SI VOUS UTILISEZ UN ENVIRONNEMENT VIRTUEL. SINON, PASSEZ A L ETAPE 3 : 
* Activer l'environnement :
```
    $ cd emi_pokedex
    
    $ nom_de_votre_venv/bin/activate
```

* Désactiver l'environnement :
```
    $ deactivate
```

* Récupérer la base de données :
```
    $ py .\manage.py migrate
```

* Exécutez le serveur de développement :
```
    $ cd emi_pokedex\EMI_Poke_app

    $ py .\manage.py runserver
```
***
# Accessibilité

Pour accéder à l'application, il faut se rendre à l'URL :

>http://127.0.0.1:8000/
