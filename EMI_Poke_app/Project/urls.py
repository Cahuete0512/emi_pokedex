from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('result/<int:number>/', views.result, name="result"),
    path('naviguer/', views.naviguerEntrePokemon, name="naviguerEntrePokemon"),
    path('equipe_1/', views.equipe, name="cartesEquipe_1"),
    path('equipe_2/', views.equipe, name="cartesEquipe_2"),
    path('equipe_3/', views.equipe, name="cartesEquipe_3"),
    path('equipe_4/', views.equipe, name="cartesEquipe_4"),
    path('equipe_5/', views.equipe, name="cartesEquipe_5")

]
