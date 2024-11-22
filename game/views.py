from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from api import get_questions, MAIN_CATEGORIES, get_main_categories, get_subcategories  # Impordib vajalikud funktsioonid api.py failist

def index(request):
    """
    Renderdab avalehe (index.html).

    See vaade tõmbab peakategooriad ja edastab need mallile.
    """
    categories = get_main_categories()  # Tõmbab peakategooriad api.py failist
    context = {'categories': categories}  # Loo konteksti sõnastiku, mis sisaldab kategooriaid
    return render(request, "index.html", context)  # Renderdab index.html malli koos kontekstiga


def options(request, category_name):
    """
    Renderdab valikute lehe (options.html).

    See vaade tõmbab alamkategooriad (kui need on olemas) ja edastab need koos muude valikutega mallile.
    """
    subcategories = get_subcategories(category_name) or {}  # Tõmbab alamkategooriad, kui neid pole, kasutab tühja sõnastikku
    context = {
        'category_name': category_name,  # Edastab peakategooria nime
        'subcategories': subcategories,  # Edastab alamkategooriad
        'difficulty_choices': ['easy', 'medium', 'hard'],  # Raskusastmete valikud
        'type_choices': ['multiple', 'boolean']  # Küsimuste tüüpide valikud
    }
    return render(request, "options.html", context)  # Renderdab options.html malli koos kontekstiga


def game(request):
    """
    Renderdab mängu lehe (game.html).

api-new1
    See vaade tõmbab küsimused API-st vastavalt kasutaja valikutele ja edastab need mallile.
    """
    category_name = request.GET.get('category')  # Saab peakategooria nime päringu parameetritest
    subcategory_name = request.GET.get('subcategory')  # Saab alamkategooria nime päringu parameetritest
    difficulty = request.GET.get('difficulty')  # Saab raskusastme päringu parameetritest
    type = request.GET.get('type')  # Saab küsimuse tüübi päringu parameetritest

    if subcategory_name:
        # Kui alamkategooria on valitud, saab selle ID MAIN_CATEGORIES sõnastikust
        category_id = MAIN_CATEGORIES.get(category_name, {}).get(subcategory_name)
    else:
        # Kui alamkategooriat pole valitud, saab peakategooria ID MAIN_CATEGORIES sõnastikust
        category_id = MAIN_CATEGORIES.get(category_name)

    questions = get_questions(  # Tõmbab küsimused API-st, kasutades get_questions() funktsiooni
        amount=15,
        category=category_id,
        difficulty=difficulty,
        type=type
    )

    if questions:
        # Kui küsimused on edukalt tõmmatud, renderdatakse game.html mall koos küsimustega
        context = {'questions': questions}
        return render(request, 'game.html', context)
    else:
        # Kui küsimuste tõmbamisel on viga, logitakse see ja renderdatakse error.html mall
        print("Error fetching questions from API.")
        return render(request, 'error.html')

def login_user(request):
    return render(request, 'registration/login.html')


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
        username = name
        User.objects.create_user(username=username, email=email, password=password)
        return HttpResponse(f'Welcome, {name}! Your account has been created successfully.<br><a href="/game/">Start the game</a>')
    return render(request, "signup.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('index')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('index')







