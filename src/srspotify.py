from flask import Flask, request, jsonify, json
from flask_cors import CORS



app = Flask(__name__)

CORS(app)

@app.route("/")
def get_channel_list():
    # automatically GET, return a list of channels
    
    json_channel_list
    return json_channel_list