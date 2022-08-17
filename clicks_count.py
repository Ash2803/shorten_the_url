import requests
import os
from dotenv import load_dotenv


def shorten_link(token, url):
    bitlink = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    body = {
        'long_url': url
    }
    response = requests.post(bitlink, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['link']


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TOKEN')
    url = input()
    print('Битлинк', shorten_link(token, url))
