import pymongo, time, bson

db = pymongo.Connection('localhost', 27017)['sicki']
ref = db.reference
proposal = db.proposal

refs = ref.find()
for row in refs:
    id = row.get('_id')
    for field, value in row.iteritems():
        if field != '_id':
            proposal_id = str(bson.ObjectId())
            proposal.insert({'_id': proposal_id,
                             'value': value,
                             'source': 'zotero',
                             'date': time.time(),
                             'accepted': True})
            ref.update({'_id': id}, {'$set': {field: [proposal_id]}})
