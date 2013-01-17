import pymongo
from bson.objectid import ObjectId

from getpass import getpass
from sys import argv

import re

import csv

if __name__ == '__main__':
    #passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['sicki']
    #mongo.authenticate('skapes', passwd)
 
    results = mongo.events.find ()
   
    for item in results:
        #if item['Path_BNGenus'] == 'Unspecified' and item['Path_BNSpp'] == 'Unspecified':
        #    name = item['Path_CName']
        #else:
        #    name = item['Path_BNGenus'] + ' ' + item['Path_BNSpp']
        eid_id = int (re.match ('HED_(\d+)', item['map']).group (1))
        mongo.events.update ({
                '_id': item['_id'],
                }, {
                '$set': {
                    'eid_id': eid_id
                    }
                });
 
