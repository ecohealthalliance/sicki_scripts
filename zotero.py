import pymongo
from bson.objectid import ObjectId
from pyzotero import zotero

from getpass import getpass
from sys import argv

if __name__ == '__main__':
    #passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['refs'] #test
    #mongo = pymongo.Connection('localhost', 3002)['meteor']
    #mongo.authenticate('skapes', passwd)

    library_id= '126319'
    library_type='group'
    api_key = 'TwxmBGN2hCcTrKePkXPaX9RI'
    zot = zotero.Zotero(library_id, library_type, api_key)
    items = zot.all_top ()
    for item in items:
        mongo.references.insert (item)
