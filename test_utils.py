import requests_mock

from app import app, mail
from utils import hnkarma, send_email


class TestHackerNews(object):

    def test_hacker_news_user(self):
        user_json = {
            "created": 1234,
            "id": "foobar",
            "karma": 911,
            "submitted": [
                567,
                568
            ]
        }
        with requests_mock.Mocker() as m:
            m.get('https://hacker-news.firebaseio.com/v0/user/foobar.json', json=user_json)
            assert hnkarma('foobar') == 911

    def test_hacker_news_null(self):
        with requests_mock.Mocker() as m:
            m.get('https://hacker-news.firebaseio.com/v0/user/usernothere.json', text='null')
            assert hnkarma('usernothere') is None


class TestEmail(object):
    def test_email_sending(self):
        with app.app_context(), mail.record_messages() as outbox:
            send_email('bob@foobar.com', 'body')

            assert len(outbox) == 1
            email = outbox[0]
            assert email.subject == 'Email from flasktdd'
            assert email.body == 'body'
            assert email.recipients == ['bob@foobar.com']
