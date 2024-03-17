# Module imports
import json # Responsible for json representation of data
from flask import Flask, jsonify, request # Import flask, jsonify to parse the json data, and request module

# Initialising the flask App by assigning flask on app variabe
app = Flask(__name__)

greeting ={
 "Joseph": {
    "Age": 27,
    "Gender": "Male"
  },
  "Marko": {
    "Age": 22,
    "Gender": "Male"
  }
}

# Basic Route to run flask app
@app.route("/user/<string:name>", methods=['GET'])
def HelloWorld():
    return jsonify(greeting)

if __name__ == '__main__':
  # Disable Debug on Production Ready Server
  # Use .env files or Secrets in GitHub action to protect the app from spoofing
   app.run(debug=True, port=5000)