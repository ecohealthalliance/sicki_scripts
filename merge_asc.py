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

    file = open ('../sicki_maps/merge.asc', 'r')
    geodata = file.read ()

    mongo.maps.insert ({
            'name': 'locations',
            'type': 'asc',
            'map': geodata
            })
