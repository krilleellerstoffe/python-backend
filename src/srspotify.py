from flask import Flask, request, jsonify, json
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

@app.route("/")
def get_channel_list():
    # automatically GET, return a list of stations
    response = requests.get('http://api.sr.se/api/v2/channels/?format=json&size=52')
    return response.json()

@app.route("/channels/<id>")
def get_channel(id):
    # returns info about current/prev/next songs for a specific station
    response = requests.get('http://api.sr.se/api/v2/playlists/rightnow?format=json&channelid=' + id)
    return response.json()

@app.route("/channels/<id>/current")
def get_current_song(id):
    # returns info on currently playing track for a given station
    response = requests.get('http://api.sr.se/api/v2/playlists/rightnow?format=json&channelid=' + id)
    return response.json()['playlist']['song']

@app.route("/channels/<id>/previous")
def get_next_song(id):
    # returns info on previously played track for a given station
    response = requests.get('http://api.sr.se/api/v2/playlists/rightnow?format=json&channelid=' + id)
    return response.json()['playlist']['previoussong']
    
@app.route("/channels/<id>/<date>")
def get_todays_playlist(id, date):
    # returns a list of tracks for a given station and date
    response = requests.get('http://api.sr.se/api/v2/playlists/getplaylistbychannelid?format=json&id=' + id + '&startdatetime=' + date)
    return response.json()

@app.route("/add", methods =["POST"]) #json body required with playlist name, track list
def create_playlist():
    # add a playlist to spotify, login required!!
    requests.post('spotify')
    return

@app.route("/add/<playlist>") #json body with song info
def add_to_playlist(playlist):
    #add song to a given playlist, login required!!
    requests.post('spotify')
    return
