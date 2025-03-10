#!/usr/bin/python3
"""
    task 3
"""
from flask import Flask, render_template
from models import storage
from models import *
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


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    """print in if its number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd_template(n):
    return render_template('6-number_odd_or_even.html', number=n)


@app.route('/states_list', strict_slashes=False)
def get_states_list():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
