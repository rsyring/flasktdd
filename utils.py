import requests

from app import mail


def hnkarma(username):
    url = 'https://hacker-news.firebaseio.com/v0/user/{}.json'.format(username)
    resp = requests.get(url)
    user_json = resp.json()
    if user_json is None:
        return None
    return user_json['karma']


def send_email(to, body):
    mail.send_message(
        subject='Email from flasktdd',
        body=body, recipients=[to],
        sender='someone@example.com'
    )
