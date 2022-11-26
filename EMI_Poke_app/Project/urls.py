from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('pokemon/', views.api_call, name="api_call"),
    path('result/<int:number>', views.result, name="result"),
    path('naviguer/', views.naviguer_entre_pokemon, name="naviguer_entre_pokemon"),
    # FIXME : Modifier les url quand l'entité équipe sera faite par :
    #  path('equipe/equipe_1', views.equipe, name="cartesEquipe_1") et ainsi de suite pour chaque équipe
    path('listEquipe/', views.equipe, name="list_equipes"),
    path('viewEquipe/<int:id>', views.equipe_details, name="equipe_details"),
    path('update_equipe/<int:id>', views.update_equipe, name="update_equipe"),
    path('delete_equipe/<int:id>', views.delete_equipe, name="delete_equipe"),
    path('create_equipe/', views.create_equipe, name="create_equipe"),

]
