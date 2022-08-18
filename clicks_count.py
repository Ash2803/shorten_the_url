import os

import requests
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


def count_clicks(token, link):
    bitlink = 'https://api-ssl.bitly.com/v4/shorten'
    link = 'https://mail.ru/'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.post(bitlink, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    url = input("Enter the url: ")
    link = 'https://mail.ru/'
    try:
        print('Битлинк', shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print("Введен неправильный URL")
    print(count_clicks(token, link))


if __name__ == '__main__':
    main()
