import flask_webtest
import mock

from app import mail
from views import app


class TestWebViews(object):
    @classmethod
    def setup_class(self):
        # The ta object can be used to make browser-like requests against our application.
        self.ta = flask_webtest.TestApp(app)

    def test_hello_world(self):
        resp = self.ta.get('/')
        assert 'Hello, World!' in resp

    def test_hello_fred(self):
        resp = self.ta.get('/hello/Fred')
        assert 'Hello, Fred!' in resp
        assert 'Hacker News' not in resp

    def test_hacker_news_lookup(self):
        with mock.patch('views.hnkarma') as m_hnkarma:
            m_hnkarma.return_value = 7
            resp = self.ta.get('/hello/rsyring?hnk=1')
        assert 'Hello, rsyring!' in resp
        assert 'Hacker News karma: 7' in resp

    def test_email_hello_1(self):
        with mail.record_messages() as outbox:
            self.ta.get('/hello/rsyring?deliver_to=randy@thesyrings.us')

            assert len(outbox) == 1
            email = outbox[0]
            assert email.subject == 'Email from flasktdd'
            assert email.body == 'Hello, rsyring!'
            assert email.recipients == ['randy@thesyrings.us']

    def test_email_hello_2(self):
        with mock.patch('views.send_email') as m_send_email:
            resp = self.ta.get('/hello/rsyring?deliver_to=randy@thesyrings.us')

            m_send_email.assert_called_once_with('randy@thesyrings.us', 'Hello, rsyring!')

        assert 'Email hello delivered to: randy@thesyrings.us' in resp
