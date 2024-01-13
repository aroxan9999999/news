import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
API_URL = 'https://newsapi.org/v2/top-headlines'


def get_news(language='en'):
    params = {
        'language': language,
        'apiKey': API_KEY
    }
    response = requests.get(API_URL, params=params)
    return response.json()
