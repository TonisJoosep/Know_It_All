import requests

from APIResponse import Response
from Category import MAIN_CATEGORIES

API_URL = "https://opentdb.com/api.php"


def get_questions(amount=int, category=int, difficulty=str, token=None):
    """
    Fetches questions from the Open Trivia DB API.

    Args:
        amount (int): The number of questions to retrieve (default: 10).
        category (str): The category of questions (optional).
        difficulty (str): The difficulty of questions ("easy", "medium", "hard") (optional).
        token (str): The session token (optional).

    Returns:
        list: A list of questions (dictionaries) on success.

    Raises:
        Response: If there's an error with the API request or response.
    """
    params = {'amount': amount}
    if category:
        if category in MAIN_CATEGORIES:  # Check if the category is valid
            params['category'] = MAIN_CATEGORIES[category]
        else:
            raise Response(f"Category not found: {category}", Response.INVALID_PARAMETER)
    if difficulty:
        params['difficulty'] = difficulty
    if token:
        params['token'] = token

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise HTTP errors
        data = response.json()

        response_code = data['response_code']
        if response_code == Response.SUCCESS:
            return data['results']
        elif response_code == Response.NO_RESULTS:
            raise Response("Not enough questions for this query.", Response.NO_RESULTS)
        elif response_code == Response.INVALID_PARAMETER:
            raise Response("Invalid parameter in the request.", Response.INVALID_PARAMETER)
        # ... handle other response codes ...
        else:
            raise Response(f"Unknown response code: {response_code}", response_code)

    except requests.exceptions.RequestException as e:
        raise Response(f"Error sending API request: {e}")
