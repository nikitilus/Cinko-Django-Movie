from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('create_set/', views.set_create, name='create_set'),
    path('create_film/', views.film_create, name='create_film'),
    path('films/', views.films, name='films'),
    
]
