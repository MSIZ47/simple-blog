from django.shortcuts import render
from django.http import HttpResponse


def say_pizza(request):
    return HttpResponse('hello_pizza')
