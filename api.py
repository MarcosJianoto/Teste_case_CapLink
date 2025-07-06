import requests

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"


def error_fetch_data(url):
    print(f"Erro ao buscar dados da seguinte URL: {url}")
    return []


def fetch_users_posts(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return error_fetch_data(url)


def fetch_users():
    return fetch_users_posts(URL_USERS)


def fetch_posts():
    return fetch_users_posts(URL_POSTS)
