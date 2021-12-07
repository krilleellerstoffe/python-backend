from flask import Flask, request, jsonify, json
from flask_cors import CORS
import requests



app = Flask(__name__)

CORS(app)

@app.route("/")
def get_channel_list():
    # automatically GET, return a list of channels
    response = requests.get('http://api.sr.se/api/v2/channels/?format=json&size=10')
    return response.json()

@app.route("/channels/<id>")
def get_channel(id):
    response = requests.get('http://api.sr.se/api/v2/playlists/rightnow?format=json&channelid=' + id)
    return response.json()