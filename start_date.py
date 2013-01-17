import pymongo
from bson.objectid import ObjectId

from getpass import getpass
from sys import argv

import csv

if __name__ == '__main__':
    passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['db_skapes']
    mongo.authenticate('skapes', passwd)
 
    results = mongo.orig_events.find ()
   
    for item in results:
        mongo.events.update ({
                'ref': item['_id'],
                }, {
                '$set': {
                    'start_date':item['PathEmerge_Date']
                    }
                });
 
