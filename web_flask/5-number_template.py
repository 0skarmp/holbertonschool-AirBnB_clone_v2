#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ return a hello string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def home2():
    """ Return a hbnb string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def page3(text):
    """ returns a string depending on the text they give us as an argument """
    new_text = text.replace('_', ' ')
    return f"C {new_text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def page4(text='is cool'):
    """ returns a string depending on the text they give us as an argument """
    new_text = text.replace('_', ' ')
    return f"Python {new_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def page5(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def page6(n):
    if isinstance(n, int):
        return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
