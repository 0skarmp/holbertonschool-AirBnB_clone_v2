#!/usr/nin/python3
"""script to start a flask web"""

from flask import Flask, render_template
app = Flask(__name__)


# route 1:
@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


# route 2:
@app.route("/hbnb", strict_slashes=False)
def page2():
    return "HBNB"


# route 3:
@app.route("/c/<text>", strict_slashes=False)
def page3(text):
    text = text.replace("_", " ")
    return f"C {text}"


# route 4:
@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def page4(text="is_cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


# route 5:
@app.route("/number/<int:n>", strict_slashes=False)
def page5(n):
    if isinstance(n, int):
        return f"{n}is a number"


@app.route("/number_template <int:n>", strict_slashes=False)
def page6(n):
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
