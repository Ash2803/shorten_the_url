import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


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
    return response.json()['id']


def count_clicks(token, link):
    bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.get(bitlink, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    long_url = input("Enter the url: ")
    print(shorten_link(token, long_url))
    try:
        print('Битлинк', shorten_link(token, long_url))
    except requests.exceptions.HTTPError:
        print("Введен неправильный URL")
    # link = shorten_link(token, long_url)
    # print(count_clicks(token, link))


if __name__ == '__main__':
    main()
