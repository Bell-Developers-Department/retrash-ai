from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/image", methods=["POST"])
def hello_world():
    print(request.json)
    return "jej"