from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('naviguer/', views.naviguer_entre_pokemon, name="naviguer_entre_pokemon"),
    path('list_equipe/', views.equipe, name="list_equipes"),
    path('view_equipe/<int:id>', views.equipe_details, name="equipe_details"),
    path('create_equipe/', views.create_equipe, name="create_equipe"),
    path('update_equipe/<int:id>', views.update_equipe, name="update_equipe"),
    path('delete_equipe/<int:id>', views.delete_equipe, name="delete_equipe"),

]
