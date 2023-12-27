#!/usr/bin/python3
from flask import Flask
""" /c/<text> """
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """ C <text> """
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
