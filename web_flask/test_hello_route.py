from flask import request

BASE = "http://127.0.0.1:5000/"

response = request.get(BASE + "greeting")
print(response.json)