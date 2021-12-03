# -*- coding: utf-8 -*-

import re
from flask import Flask, jsonify, json
from flask import request
from flask.helpers import make_response
from flask.templating import render_template

from unicorns import storage
from unicorns.Unicorn import Unicorn

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    # automatically GET, return a list of unicorns
    if request.method == 'GET':
        unicornsList = storage.fetch_unicorns()
        unicornsText = []
        for unicorn in unicornsList:
            unicornsText.append(unicorn.to_dict())
        if request.headers.get('Accept') == 'application/json':
            unicornJSON = jsonify(unicornsText)
            return unicornJSON
        else:
            return f"{unicornsText}"
    elif request.method == 'POST':
        unicorn = json_to_unicorn(request.get_json())
        storage.add_unicorn(unicorn)
        return "Posted"
    else:
        return "Invalid method"

@app.route("/<id>", methods=['GET', 'PUT', 'DELETE'])
def unicornId(id):
    if request.method == 'GET':
        unicornText = storage.fetch_unicorn(id).to_dict()
        if request.headers.get('Accept') == 'application/json':
            unicornJSON = jsonify(unicornText)
            return unicornJSON
        elif request.headers.get('Accept') == 'text/html':
            request.make_response 
    elif request.method == 'PUT':
        unicorn = json_to_unicorn(request.get_json())
        storage.update_unicorn(unicorn)
        return "Put"
    elif request.method == 'DELETE':
        storage.delete_unicorn(id)
        return "Delete"
    else:
        return "Invalid method"

def json_to_unicorn(data: dict) -> Unicorn:
    '''
    Genom att hantera all JSON -> Unicorn på ett och samma ställe minskar vi
    risken för fel och kommer undan med lite mindre kod. Funktionen anropas av
    add_unicorn() och i update_unicorn().
    '''
    
    unicorn = Unicorn()
    if 'id' in data:
        unicorn.id = data['id']
    unicorn.name = data['name']
    unicorn.description = data['description']
    unicorn.reported_by = data['reportedBy']
    unicorn.spotted_where.name = data['spottedWhereName']
    unicorn.spotted_where.lat = data['spottedWhereLat']
    unicorn.spotted_where.lon = data['spottedWhereLon']
    unicorn.spotted_when = data['spottedWhen']
    unicorn.image = data['image']
    
    return unicorn
