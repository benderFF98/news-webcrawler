import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.environ.get('API_BASE_URL', 'http://localhost:8000')


def create_article(title, text, source, url_article):
    """
    Create an article via a POST request to the API.

    Args:
        title (str): The title of the article.
        text (str): The text/content of the article.
        source (str): The source of the article.
        url_article (str): The URL of the article.

    Returns:
        requests.Response: The response object from the POST request.
    """
    try:
        api_endpoint = '/api/articles'  # Define the API endpoint path
        url = f'{base_url}{api_endpoint}'

        data = {
            'title': title,
            'text': text,
            'source': source,
            'url': url_article
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx and 5xx status codes)
        return response
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None
