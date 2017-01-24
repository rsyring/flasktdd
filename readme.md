Getting Started
===============

1. Creating a [virtualenv][1] for this project is recommended.
2. Install initial dependencies:

    ```shell
    $ pip install flask flask-webtest pytest

    <...snip...>

    Successfully installed Jinja2-2.9.4 MarkupSafe-0.23 WebOb-1.7.1 WebTest-2.0.24
    Werkzeug-0.11.15 beautifulsoup4-4.5.3 blinker-1.4 click-6.7 flask-0.12 flask-webtest-0.0.8
    itsdangerous-0.24 py-1.4.32 pytest-3.0.6 waitress-1.0.1
    $
    ```

4. Profit!

    ```shell
    $ py.test
    .
    1 passed in 0.13 seconds
    ```

[1]: https://pypi.python.org/pypi/virtualenv

Our Tools
==============

Getting to know your tools is really important:

1. [Flask: our web framework](https://flask.pocoo.org/)
2. [WebTest: library for testing WSGI applications](https://webtest.readthedocs.io/en/latest/)
3. [Flask-WebTest: eases testing Flask apps w/ WebTest](https://flask-webtest.readthedocs.io/en/latest/)
4. [py.test](http://docs.pytest.org/en/latest/)
