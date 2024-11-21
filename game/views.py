from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def game(request):
    return HttpResponse("Welcome to the game")


def index(request):
    return render(request, "index.html")


def options(request, category_id=None):
    if category_id:
        return render(request, "options.html", {'category_id': category_id})
    else:
        return render(request, 'options.html', {'message': 'No category selected.'})


def login(request):
    return render(request, "login.html")


def forgot_password(request):
    return render(request, "forgot_password.html")


def register(request):
    return render(request, "signup.html")


def reset_password(request):
    return render(request, "reset_password.html")


def signup(request):
    return render(request, "signup.html")


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return HttpResponse("Passwords do not match!<br><a href='/signup'>Try again</a>")

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists<br><a href='/signup'>Try again</a>")

        username = email.split('@')[0]
        User.objects.create_user(username=username, email=email, password=make_password(password))
        return HttpResponse(f'Welcome, {name}! Your account has been created successfully.<br><a href="/game/">Login</a>')
    return render(request, "signup.html")

