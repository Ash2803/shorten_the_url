import os

import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(token, url):
    """Make short url from given long url"""
    short_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    body = {
        'long_url': url
    }
    response = requests.post(short_url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    """Parse url from def shorten_link and count amount of clicks on it"""
    parsed_link = urlparse(link)
    unparsed_link = ''.join(parsed_link[1:])
    num_of_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{unparsed_link}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    params = {
        'unit': 'day',
        'units': '-1'
    }
    response = requests.get(num_of_clicks, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return clicks_count


def is_bitlink(url, token):
    parsed_link = urlparse(url)
    unparsed_link = ''.join(parsed_link[1:])
    bitlink = f'https://api-ssl.bitly.com/v4/bitlinks/{unparsed_link}'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(bitlink, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    url = input("Введите ссылку: ")
    try:
        if is_bitlink(url, token):
            print(count_clicks(token, url))
        else:
            print(shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print("Введена неправильная ссылка")


if __name__ == '__main__':
    main()
