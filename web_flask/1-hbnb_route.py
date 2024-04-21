#!/usr/bin/python3
"""
This is a multi-route Flask App that return
Route A: '/'
Route B: '/HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    End-point that displays 'Hello HBNB'
    """
    return "Hello HBNB!"


@app.rout('/hbnb', strick_slashes=False)
def hbnb():
    """
    End-point that displays "HBNB"
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

