#!/usr/bin/python3
""" script to start a flask web"""

from flask import Flask
app = Flask(__name__)


# route 1:
@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


# route 2:
@app.route("/hbnb", strict_slashes=False)
def page2():
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
