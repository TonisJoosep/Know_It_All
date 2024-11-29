from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .api.client import get_questions
from .api.category import MAIN_CATEGORIES, get_main_categories, get_subcategories
import random
import json
from django.contrib.auth.decorators import login_required
from.models import GameHistory
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    '''
    Renderdab avalehe (index.html).

    See vaade tõmbab peakategooriad ja edastab need mallile.
    '''
    categories = get_main_categories()
    context = {'categories': categories}
    return render(request, 'index.html', context)


def options(request, category_name):
    '''
    Renderdab valikute lehe (options.html).

    See vaade tõmbab alamkategooriad (kui need on olemas)
    ja edastab need koos muude valikutega mallile.
    '''
    subcategories = get_subcategories(category_name) or {}
    context = {
        'category_name': category_name,
        'subcategories': subcategories,
        'difficulty_choices': ['easy', 'medium', 'hard'],
    }
    return render(request, 'options.html', context)

@login_required
def game(request):
    '''
    Renderdab mängu lehe (game.html).

    See vaade tõmbab küsimused API-st vastavalt kasutaja
    valikutele ja edastab need mallile.
    '''
    category_name = request.GET.get('category')
    subcategory_name = request.GET.get('subcategory')
    difficulty = request.GET.get('difficulty')
    amount = request.GET.get('amount')

    if not amount:
        amount = 10
    else:
        amount = int(amount)

    if subcategory_name:
        category_id = MAIN_CATEGORIES.get(category_name, {}).get(subcategory_name)
    else:
        category_id = MAIN_CATEGORIES.get(category_name)

    questions = get_questions(
        amount=amount,
        category=category_id,
        difficulty=difficulty,
    )
    difficulty_multipliers = {
        'easy': 1,
        'medium': 1.5,
        'hard': 2,
    }
    multiplier = difficulty_multipliers.get(difficulty, 1)

    if questions:
        for question in questions:
            incorrect_answers = question.get('incorrect_answers', [])
            correct_answers = question.get('correct_answer')
            all_answers = incorrect_answers + [correct_answers]
            random.shuffle(all_answers)
            question['shuffled_answers'] = all_answers

        total_score = 0
        for question in questions:
            if 'user_answer' in question and question['user_answer'] == question['correct_answer']:
                total_score += 10
        total_score *= multiplier
        context = {
            'questions': questions,
            'total_score': total_score,
            'difficulty': difficulty,
            'multiplier': multiplier,
        }
        return render(request, 'game.html', context)

    print('Error fetching questions from API.')
    return render(request, 'error.html')


def login_user(request):
    return render(request, 'registration/login.html')


def forgot_password(request):
    if request.method == "POST":
        request.POST.get("email")
        messages.success(request, "Password reset email has been sent.")
        return redirect('index')
    return render(request, 'forgot_password.html')


def register(request):
    return render(request, 'signup.html')


def signup(request):
    return render(request, 'signup.html')


def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Password doesn't match.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')
        username = name
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, f'Welcome {name}, Your account has been created successfully.')
        return redirect('index')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('index')
        messages.error(request, 'Invalid Username or Password')
        return redirect('login')
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form, 'show_header': False})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('index')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def privacy(request):
    return render(request, 'privacy.html')


@login_required  # Ensure only authenticated users can save their scores
@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            category = data.get('category')
            difficulty = data.get('difficulty')
            score = data.get('score')

            # Save the game history
            GameHistory.objects.create(
                user=request.user,
                category=category,
                difficulty=difficulty,
                score=score,
            )
            return JsonResponse({'message': 'Score saved successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


@login_required
def leaderboard(request):
    scores = GameHistory.objects.filter(user=request.user).order_by('-score')[:10]  # Top 10 scores for the user
    return render(request, 'leaderboard.html', {'scores': scores})