import pymongo

db = pymongo.Connection('localhost', 27017)['sicki']
eid = db.eid
proposal = db.proposal

eid_events = eid.find()
for row in eid_events:
    id = row.get('_id')
    for field, value in row.iteritems():
        if field != '_id' and field != 'jones' and field != 'orig_event' and field != 'references':
            proposal_ids = []
            for pid in value:
                proposal_ids.append(str(pid))
            changes = {}
            changes[field] = proposal_ids
            eid.update({'_id': id}, {'$set': changes})

proposals = proposal.find()
for row in proposals:
    id = row.get('_id')
    row['_id'] = str(id)
    proposal.remove({'_id': id})
    proposal.insert(row)
