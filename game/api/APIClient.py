import requests
import logging

API_URL = "https://opentdb.com/api.php"

logger = logging.getLogger(__name__)

def get_questions(amount, category=None, difficulty=None, type=None):
    """
    Tõmbab küsimused API-st.
    """
    try:
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
        data = response.json()

        if 'results' not in data:
            raise KeyError("'results' key not found in API response")

        return data["results"]

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching questions: {e}")
        return None
    except KeyError as e:
        logger.error(f"Error parsing API response: {e}")
        raise