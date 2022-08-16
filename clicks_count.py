import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
url = 'https://api-ssl.bitly.com/v4/user'
headers = {
    'Authorization': f'Bearer {token}'
}


def get_user_info():
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.json())


url2 = 'https://api-ssl.bitly.com/v4/shorten'
body = {
    'long_url': 'https://mail.ru/',
}


def get_shorten_link():
    response = requests.post(url2, headers=headers, json=body)
    response.raise_for_status()
    print(response.json())


get_shorten_link()
