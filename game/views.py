from django.shortcuts import render  # Impordib render funktsiooni mallide renderdamiseks
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

def login(request):
    return render(request, "login.html")


