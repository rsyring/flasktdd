import requests


def hnkarma(username):
    url = 'https://hacker-news.firebaseio.com/v0/user/{}.json'.format(username)
    resp = requests.get(url)
    user_json = resp.json()
    if user_json is None:
        return None
    return user_json['karma']
