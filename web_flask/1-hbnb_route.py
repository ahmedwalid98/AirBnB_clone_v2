#!/usr/bin/python3
"""
    task 2
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
