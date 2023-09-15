#!/usr/bin/python3
""" script to start a flask web"""

app = Flask(__name__)


@app.route("/hbnb")
def home():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000", strict_slashes=False)