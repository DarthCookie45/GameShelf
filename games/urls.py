from django.urls import path

from . import views

urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('add/', views.game_create, name='game_create'),
]