from views import app


def pytest_configure(config):
    app.config['TESTING'] = True
    return app
