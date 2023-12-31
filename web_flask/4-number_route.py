#!/usr/bin/python3
""" Write a script that starts a Flask web application """

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def h_route():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    if n.isdigit():
        return f"{n} is a number"
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
