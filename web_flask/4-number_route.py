#!/usr/bin/python3
"""script to connect html with flask"""

from flask import Flask
app = Flask(__name__)


# route 1:
@app.route("/", strict_slashes=False)
def home():
    """This function returns a greeting on the home page."""
    return "Hello HBNB!"


# route 2:
@app.route("/hbnb", strict_slashes=False)
def page2():
    """This function returns 'HBNB'."""
    return "HBNB"


# route 3:
@app.route("/c/<text>", strict_slashes=False)
def page3(text):
    """This function takes a 'text' parameter and displays it on the page."""
    text = text.replace("_", " ")
    return f"C {text}"


# route 4:
@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def page4(text="is_cool"):
    """function,text parameter & displays'Python{text}'on another the page."""
    text = text.replace("_", " ")
    return f"Python {text}"


# route 5:
@app.route("/number/<int=n>", strict_slashes=False)
def page5(n):
    """function takes an integer'n'& displays if it is a number on the page."""
    if isinstance(n, int):
        return f"{n}is a number"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
