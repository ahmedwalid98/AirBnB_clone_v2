#!/usr/bin/python3
"""
    task 3
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ returns hello hbnh"""
    return "Hello HBNB!"


@app.route('/hbnb/', strict_slashes=False)
def only_hbnb():
    """ returns hbnh"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def print_c(text):
    """returns text from url"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python(text):
    """returns text from url"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
