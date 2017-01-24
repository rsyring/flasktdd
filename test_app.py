import flask_webtest
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
