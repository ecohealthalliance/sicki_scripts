import pymongo, time

db = pymongo.Connection('localhost', 27017)['sicki']
eid = db.eid
proposal = db.proposal

eid_events = eid.find()
for row in eid_events:
    id = row.get('_id')
    for field, value in row.iteritems():
        if field == 'pathogens':
            proposal_ids = []
            for pathogen in value:
                proposal_id = proposal.insert({'value': pathogen,
                                               'source': 'original_data',
                                               'date': time.time(),
                                               'accepted': True})
                proposal_ids.append(proposal_id)
            eid.update({'_id': id}, {'$set': {'pathogens': proposal_ids}})
            
        elif field != '_id' and field != 'jones' and field != 'orig_event' and field != 'references':
            proposal_id = proposal.insert({'value': value,
                                           'source': 'original_data',
                                           'date': time.time(),
                                           'accepted': True})
            eid.update({'_id': id}, {'$set': {field: [proposal_id]}})
    
