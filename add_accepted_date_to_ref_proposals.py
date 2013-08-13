import pymongo

db = pymongo.Connection('localhost', 27017)['sicki']
proposal = db.proposal

proposals = proposal.find({'source': 'zotero'})

for row in proposals:
    id = row.get('_id')
    date = row.get('date')
    proposal.update({'_id': id}, {'$set': {'accepted_date': date}})
