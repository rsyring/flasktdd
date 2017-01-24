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

Next Steps
==========

Using TDD and without ever running the application:

1. Create a Flask view to say "Hello, World!"
2. Create a Flask view to say "Hello, `$name`!" where `$name` comes from a URL: "/hello/Fred"
3. Optionally request $name from the Hacker News user API, if present, display Karma.
4. Optionally send email hello instead of displaying on the screen.

Our Tools
==============

Getting to know your tools is really important:

1. [Flask: our web framework](https://flask.pocoo.org/)
2. [WebTest: library for testing WSGI applications](https://webtest.readthedocs.io/en/latest/)
3. [Flask-WebTest: eases testing Flask apps w/ WebTest](https://flask-webtest.readthedocs.io/en/latest/)
4. [py.test](http://docs.pytest.org/en/latest/)
5. [Requests]()
6. [Requests Mock](https://requests-mock.readthedocs.io/en/latest/)
7. [Mock](https://docs.python.org/dev/library/unittest.mock.html)
8. [Flask Mail](http://pythonhosted.org/Flask-Mail/)
