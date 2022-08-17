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


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    url = input("Enter the url: ")
    try:
        print('Битлинк', shorten_link(token, url))
    except requests.exceptions.HTTPError:
        print("Введен неправильный URL")


if __name__ == '__main__':
    main()

