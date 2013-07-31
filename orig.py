import pymongo
from bson.objectid import ObjectId

#from getpass import getpass
from sys import argv

import csv

def load_csv (path):
    reader = csv.reader (open (path, "r"))
    header = reader.next ()
    values = []
    for line in reader:
        item = {}
        for key, value in zip (header, line):
            item[key] = value
        values.append (item)
    return values

if __name__ == '__main__':
#    passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['sicki']
#    mongo.authenticate('skapes', passwd)
    
    data = load_csv (argv[1])
    for item in data:
        mongo.orig_events.insert (item)
