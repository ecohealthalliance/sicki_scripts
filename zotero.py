import pymongo
from bson.objectid import ObjectId
from pyzotero import zotero

from getpass import getpass
from sys import argv

if __name__ == '__main__':
    passwd = getpass ("Password: ")
    mongo = pymongo.Connection ('localhost', 27017)['db_skapes']
    mongo.authenticate('skapes', passwd)

    library_id= '77783'
    library_type='group'
    api_key = 'hT2SLlqonWyD1253s93zg3bC'
    zot = zotero.Zotero(library_id, library_type, api_key)
    items = zot.all_top ()
    for item in items:
        mongo.refs.insert (item)
