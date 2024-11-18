from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

def game(request):
    return HttpResponse("Welcome to the game")

def index(request):
    return render(request, "index.html")

def options(request, category_id):
    return render(request, "options.html")

def login(request):
    return render(request, "login.html")


