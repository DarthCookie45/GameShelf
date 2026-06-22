from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/email/', views.edit_email, name='edit_email'),
    path('logout/', views.logout_user, name='logout'),
]