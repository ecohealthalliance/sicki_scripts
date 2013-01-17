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
        if item['Path_BNGenus'] == 'Unspecified' and item['Path_BNSpp'] == 'Unspecified':
            name = item['Path_CName']
        else:
            name = item['Path_BNGenus'] + ' ' + item['Path_BNSpp']
        mongo.events.update ({
                'ref': item['_id'],
                }, {
                '$set': {
                    'event_name': ' - '.join ([item['PathEmerge_Date_Yr'], item['PathEmerge_Location'], name])
                    }
                });
 
