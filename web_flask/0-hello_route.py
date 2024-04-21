#!/usr/bin/python3
from . import create_app

app = create_app()

@app.route('/', strict_slashes=False)
def hello_HBNB():
  """
    Route Definitation that returns a string "Hello HBNB!' when GET request is call through port 5000
  """
  return "Hello HBNB!"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)