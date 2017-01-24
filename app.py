from flask import Flask, request
from utils import hnkarma

app = Flask(__name__)


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
