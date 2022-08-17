import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    body = {
        'long_url': 'https://mail.ru/',
    }
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    print('Битлинк', response.json()['link'])


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')
    url = 'https://api-ssl.bitly.com/v4/shorten'
    shorten_link(token, url)
