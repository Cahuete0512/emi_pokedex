from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('result/<int:number>/', views.result, name="result"),
    path('naviguer/', views.naviguerEntrePokemon, name="naviguerEntrePokemon"),
    path('equipe_1/', views.equipe_1, name="cartesEquipe_1"),
    path('equipe_2/', views.equipe_2, name="cartesEquipe_2"),
    path('equipe_3/', views.equipe_3, name="cartesEquipe_3"),
    path('equipe_4/', views.equipe_4, name="cartesEquipe_4"),
    path('equipe_5/', views.equipe_5, name="cartesEquipe_5")
]
