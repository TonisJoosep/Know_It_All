import requests
import logging

from know_it_all.settings import API_URL

logger = logging.getLogger(__name__)

def get_questions(amount, category=None, difficulty=None):
    '''
    Tõmbab küsimused API-st.
    '''
    try:
        params = {
            'amount': amount,
        }
        if category:
            params['category'] = category
        if difficulty:
            params['difficulty'] = difficulty


        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        return data.get('results')

    except requests.exceptions.RequestException as e:
        logger.error(f'Error fetching questions: {e}')
        return None
