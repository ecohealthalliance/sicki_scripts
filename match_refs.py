import pymongo

import csv
from sys import argv

import simplejson as json

mongo = pymongo.Connection ('localhost', 27017)['sicki']

if __name__ == '__main__':
    pathname = argv[1]
    file = open (pathname, "r")
    reader = csv.reader (file, delimiter = ',')
    head = reader.next ()
    for next in reader:
        refs = json.loads (next[17])
        for ref in refs:
            reference = mongo.refs.find_one ({'rights': int (ref)})
            if reference:
                mongo.events.update ({'eid_id': int (next[1])},
                                     {'$push': {'references': reference['_id']}})
                

