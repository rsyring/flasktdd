from flask import request

from app import app
from utils import hnkarma, send_email


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello/<name>')
def hello_name(name):
    response = 'Hello, {}!'.format(name)
    if 'hnk' in request.args:
        karma = hnkarma(name)
        response += '\nHacker News karma: {}'.format(karma)
    return response
