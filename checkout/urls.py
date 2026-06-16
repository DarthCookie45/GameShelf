from django.urls import path

from . import views

urlpatterns = [
    path('premium/', views.premium, name='premium'),
]