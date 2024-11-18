import requests

API_URL = "https://opentdb.com/api.php"

def get_questions(amount=15, category=None, difficulty=None, type=None):
    """
    Get questions from the Open Trivia Database API.
    """
    params = {
        "amount": amount,
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty
    if type:
        params["type"] = type
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()["results"]
