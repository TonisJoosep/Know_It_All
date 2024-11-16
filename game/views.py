from django.shortcuts import render
from django.http import HttpResponse


def game(request):
    return HttpResponse("Welcome to the game")


