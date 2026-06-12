from django.urls import path

from . import views

urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('add/', views.game_create, name='game_create'),
    path('<int:pk>/edit/', views.game_update, name='game_update'),
    path('<int:pk>/delete/', views.game_delete, name='game_delete'),
]