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
        newUnicornJSON = request.get_json
        newUnicornAttributes = jsonify(newUnicornJSON)
        unicorn = Unicorn
        unicorn.from_db(newUnicornAttributes)
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
        return "Put"
    elif request.method == 'DELETE':
        return "Delete"
    else:
        return "Invalid method"

    