import pymongo
from bson.objectid import ObjectId

from getpass import getpass
from sys import argv

import csv

if __name__ == '__main__':
#    passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['sicki']
#    mongo.authenticate('skapes', passwd)
 
    results = mongo.orig_events.find ()
   
    for item in results:
        mongo.events.insert ({
                'ref': item['_id'],
                'event_name': ' - '.join ([item['PathEmerge_Date_Yr'], item['PathEmerge_Location'], item['Path_BNSpp']])
                });
 
