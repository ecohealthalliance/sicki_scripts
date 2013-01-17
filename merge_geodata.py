import pymongo
from bson.objectid import ObjectId

from getpass import getpass
from sys import argv

import simplejson as json

import csv

if __name__ == '__main__':
    #passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['sicki']
    #mongo.authenticate('skapes', '')
 
    results = mongo.events.find ()
   
    for item in results:
        try:
            file = open ('../sicki_maps/' + item['map'] + '.json', "r")
            geodata = json.loads (file.read ())
        except:
            geodata = None
        if geodata:
            mongo.maps.insert ({
                    'name': item['map'],
                    'type': 'json',
                    'map': geodata
                    })


 
