# -*- coding: utf-8 -*-

from .Location import Location
import json

class Unicorn:
    '''
    En enkel klass för att representera en enhörning
    '''
    
    #id = 0
    #name = ""
    #description = ""
    #reportedBy = ""
    #spottedWhere =  Location()
    #spottedWhen = 0
    #image = ""

    def __init__(self):
        self.id = 0
        self.name = ""
        self.description = ""
        self.reported_by = ""
        self.spotted_where = Location()
        self.spotted_when = 0
        self.image = ""

    def from_db(self, data):
        '''
        Populerar en enhörning med data från en databasförfrågan.
        '''
        
        self.id = data[0]
        self.name = data[1]
        self.description = data[2]
        self.reported_by = data[3]
        self.spotted_where.name = data[4]
        self.spotted_where.lat = data[5]
        self.spotted_where.lon = data[6]
        self.spotted_when = data[7]
        self.image = data[8]
    
    def to_dict(self):
        '''
        Skapar en dictionary med värden från denna enhörning. Bra att använda
        när man matar in enhörningar i databaser.
        '''
        
        return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'reportedBy': self.reported_by,
                'spottedWhereName': self.spotted_where.name,
                'spottedWhereLat': self.spotted_where.lat,
                'spottedWhereLon': self.spotted_where.lon,
                'spottedWhen': self.spotted_when,
                'image': self.image
                }
