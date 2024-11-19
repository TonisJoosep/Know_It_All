import requests
import logging

API_URL = "https://opentdb.com/api.php"

logger = logging.getLogger(__name__)  # Saab logija selle mooduli jaoks

MAIN_CATEGORIES = {  # Sõnastik, mis hoiab peamisi kategooriaid ja alamkategooriaid koos nende ID-dega
    "General Knowledge": 9,
    "Entertainment": {
        "Books": 10,
        "Film": 11,
        "Music": 12,
        "Musicals & Theatres": 13,
        "Television": 14,
        "Video Games": 15,
        "Board Games": 16,
        "Comics": 29,
        "Japanese Anime & Manga": 31,
        "Cartoon & Animations": 32,
    },
    "Science": {
        "Nature": 17,
        "Computers": 18,
        "Mathematics": 19,
        "Gadgets": 30,
    },
    "Mythology": 20,
    "Sports": 21,
    "Geography": 22,
    "History": 23,
    "Politics": 24,
    "Art": 25,
    "Celebrities": 26,
    "Animals": 27,
    "Vehicles": 28,
}

def get_main_categories():
    """
    Tagastab peamiste kategooriate nimekirja.
    """
    return list(MAIN_CATEGORIES.keys())  # Tagastab MAIN_CATEGORIES sõnastiku võtmete (kategooriate nimede) loendi


def get_subcategories(category_name):
    """
    Tagastab alamkategooriate loendi antud peakategooria jaoks.
    """
    return MAIN_CATEGORIES.get(category_name, {})  # Tagastab alamkategooriad peakategooria nime alusel,
                                                 # kui neid pole, tagastab tühja sõnastiku

def get_questions(amount=15, category=None, difficulty=None, type=None):
    """
    Tõmbab küsimused API-st.

    See funktsioon saadab GET päringu API-le, et tõmmata küsimusi vastavalt etteantud parameetritele.

    Args:
        amount: Küsimuste arv, mida tõmmata (vaikimisi: 15).
        category: Kategooria ID (või alamkategooria ID).
        difficulty: Raskusaste ('easy', 'medium', 'hard').
        type: Küsimuse tüüp ('multiple', 'boolean').

    Returns:
        Küsimuste sõnastike loendi või None, kui on viga.
    """
    try:
        params = {  # Sõnastik API päringu parameetrite jaoks
            "amount": amount,
        }
        if category:
            params["category"] = category
        if difficulty:
            params["difficulty"] = difficulty
        if type:
            params["type"] = type

        response = requests.get(API_URL, params=params)  # Saadab GET päringu koos parameetritega
        response.raise_for_status()  # Tõstab vea, kui API päring tagastab halva staatusekoodi
        data = response.json()  # Parsib JSON vastuse

        if 'results' not in data:  # Kontrollib, kas vastuses on 'results' võti
            raise KeyError("'results' key not found in API response")  # Tõstab vea, kui 'results' võtit pole

        return data["results"]  # Tagastab küsimuste loendi

    except requests.exceptions.RequestException as e:  # Püüab kinni kõik API päringuga seotud vead
        logger.error(f"Error fetching questions: {e}")  # Logib vea
        return None  # Tagastab None, et näidata viga
    except KeyError as e:  # Püüab kinni KeyErrori, kui vastuse parsimisel on probleeme
        logger.error(f"Error parsing API response: {e}")  # Logib vea
        raise  # Tõstab vea uuesti (või tagastab None)