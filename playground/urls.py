from django.contrib import admin
from django.urls import path, include
from .views import say_pizza
urlpatterns = [
    path('pizza/', say_pizza, name='pizza')
]
