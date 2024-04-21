#!/usr/bin/python3
"""
This is Flask App that returns the string "Hello HBNB" through the End-Point
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route Definitation that returns a string "Hello HBNB!'
    when GET request is call through port 5000
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
