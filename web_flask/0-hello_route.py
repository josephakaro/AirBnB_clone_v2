# Module imports
import json # Responsible for json representation of data
from flask import Flask

# Import flask, jsonify to parse the json data, and request module

# Initialising the flask App by assigning flask on app variabe
app = Flask(__name__)

# Basic Route to run flask app
@app.route("/", strict_slashes=False)
def Greetings():
    return "Hello HBNB!"

if __name__ == '__main__':
  # Disable Debug on Production Ready Server
  # Use .env files or Secrets in GitHub action to protect the app from spoofing
   app.run(host='0.0.0.0', port=5000)