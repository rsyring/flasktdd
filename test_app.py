import flask_webtest
import mock

from app import app


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
        with mock.patch('app.hnkarma') as m_hnkarma:
            m_hnkarma.return_value = 7
            resp = self.ta.get('/hello/rsyring?hnk=1')
        assert 'Hello, rsyring!' in resp
        assert 'Hacker News karma: 7' in resp

