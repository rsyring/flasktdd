import pytest

from views import app


@pytest.fixture
def test_prep():
    app.config['TESTING'] = True
    return app
