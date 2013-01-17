import pymongo
from bson.objectid import ObjectId

from getpass import getpass
from sys import argv

import csv

import simplejson as json
from shapely.geometry import asShape

if __name__ == '__main__':
    passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['db_skapes']
    mongo.authenticate('skapes', passwd)
 
    results = mongo.orig_events.find ()
   
    for item in results:
        try:
            buffer = open ('../Maps_Projected/maps/%s' % item['FileName'].replace ('.shp', '.json'))
        except:
            continue
        layer = json.loads (buffer.read ())
        feature = layer['features'][0]
        f = asShape (feature['geometry'])
        centroid = f.centroid
        mongo.events.update ({
                'ref': item['_id'],
                }, {
                '$set': {
                    'centroid': [
                        f.centroid.x,
                        f.centroid.y
                        ]
                    }
                })
 
