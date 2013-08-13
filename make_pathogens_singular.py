import pymongo

db = pymongo.Connection('localhost', 27017)['sicki']
eid = db.eid

eid_events = eid.find()
for row in eid_events:
    id = row.get('_id')
    pathogens = row.get('pathogens')
    eid.update({'_id': id}, {'$set': {'pathogen': pathogens}, '$unset': {'pathogens': ''}})
