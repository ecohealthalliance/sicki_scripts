import pymongo, datetime
from bson.objectid import ObjectId
import ast

#db = pymongo.Connection('localhost', 27017)['sicki3']
db = pymongo.Connection('localhost', 3002)['meteor']

# source collections
#economics = db.economics
event = db.event
#host = db.host
#location = db.location
#'metaData': metaData = db.'metaData': metaData
#metrics = db.metrics
#pathogen = db.pathogen

# update entries from the other collections
eid_events = event.find()

meta = {
  'rank' : {
    'eha': True,
    'expert': False,
    'top': True,
    'auto': False
  },
  'votes': {
    'up': 0, 
    'down': 0
  },
  'userId': 0,
  'reviewer': 'eha',
  'submitted': ''
}

print meta

count = 0

#dates = ['startDate','startDateISO','refStartDate','endDate','endDateISO','refEndDate']

for eid in eid_events:
    #print eid['eventName']

    count += 1

    # Load host
    cursor = db.host.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_host = value
        #print eid_host['hostTaxOrder']

    # Load economics
    cursor = db.economics.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_economics = value
        #print eid_economics['avgAgeDeath']

    # Load pathogens
    cursor = db.pathogen.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_pathogen = value
        #print eid_pathogen['pathogenClass']

    # Load locations
    cursor = db.location.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_location = value
        #print eid_location['locationNation']

    # Load SI matches
    cursor = db.match_key_si.find ({'jonesEIDID': eid['eidID']})
#    print type(db.match_key_si.findOne({}, {'jonesEIDID':1}))
    for value in cursor:    
        eid_match = value
        print eid_match['jonesEIDID']

    id = eid.get('_id')

    eid_body = {
    # Meta Data
    'meta': {
      'rank' : {
        'eha': True,
        'expert': False,
        'top': True,
        'auto': False
      },
      'votes': {
        'up': 0, 
        'down': 0
      },
      'userId': 0,
      'reviewer': eid['reviewer'],
      'submitted': ''
    },

    # Calculated fields
    'commentsCount': 0, #Calculated field
    'refsCount': 0, #Calculated field

    # Relational fields
    # populate refs when matched with the original jones refs

    'refs': ast.literal_eval(eid_match['jonesSources']), #Calculated field
    'comments' : [], #Calculated field

    # Quoted value
    'valQuote': {}, # original data from Jones et al SI

    # Value object
    'val' : {
        'sickiID':{
        'val':'',
        'valQuote': eid['eidID'],
        'ref': 'ehaID',
        'meta': meta
        },

        'eventName':{
        'val':'',
        'valQuote': eid['eventName'],
        'refBlob': eid['refEventName'],
        'ref': [],
        'meta': meta
        },

        'disease':{
        'val': eid['diseaseVal'],
        'valQuote': eid['disease'],
        'icd10':eid['ICD10Val'],    
        'ref':[],
        'refBlob': eid['refDisease'],
        'meta': meta
        },

        'eid':{
        'val':'',
        'valQuote': eid['eid'],
        'ref':[],
        'refBlob': eid['refEID'],
        'meta': meta
        },

        'eidCategory':{
        'val':'',
        'valQuote': eid['eidCategory'],
        'ref':[],
        'refBlob': eid['refEIDCategory'],
        'meta': meta
        },

        'abstract': {
        'val':'',
        'valQuote': eid['Abstract'],
        'ref':[],
        'refBlob': eid['refAbstract'],
        'meta': meta
        },

        'notes': {
        'val':'',
        'valQuote': eid['notes'],
        'ref':[],
        'refBlob': eid['refNotes'],
        'meta': meta
        },

        'transmissionModel': {
        'val':eid['transitionModelVal'],
        'valQuote': eid['transitionModel'],
        'ref':[],
        'refBlob': eid['refTransitionModel'],
        'meta': meta
        },

        'zoonoticType': {
        'val':eid['zoonoticTypeVal'],
        'valQuote': eid['zoonoticType'],
        'ref':[],
        'refBlob': eid['refZoonoticType'],
        'meta': meta
        },

        'sampleType': {
        'val':eid['sampleTypeVal'],
        'valQuote': eid['sampleType'],
        'ref':[],
        'refBlob': eid['refSampleType'],
        'meta': meta
        },

        'driver': {
        'val':eid['driverVal'],
        'valQuote': eid['driver'],
        'ref':[],
        'refBlob': eid['refDriver'],
        'meta': meta
        },
            

        ## Pathogens
        'pathogens':{
            'drugResistance': {
            'val':'',
            'valQuote': eid_pathogen['pathogenDrugResistance'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenDrugResistance'],
            'meta': meta
            },

            'reportedName': {
            'val':'',
            'valQuote': eid_pathogen['pathogenReportedName'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenReportedName'],
            'meta': meta
            },

            'class': {
            'val':'',
            'valQuote': eid_pathogen['pathogenClass'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenClass'],
            'meta': meta
            },

            'family': {
            'val':'',
            'valQuote': eid_pathogen['pathogenFamily'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenFamily'],
            'meta': meta
            },

            'species': {
            'val':'',
            'valQuote': eid_pathogen['pathogenSpecies'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenSpecies'],
            'meta': meta
            },

            'authority': {
            'val':'',
            'valQuote': eid_pathogen['pathogenAuthority'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenAuthority'],
            'meta': meta
            },

            'taxOrder': {
            'val':'',
            'valQuote': eid_pathogen['pathogenTaxOrder'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenTaxOrder'],
            'meta': meta
            },

            'genus': {
            'val':'',
            'valQuote': eid_pathogen['pathogenGenus'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenGenus'],
            'meta': meta
            },

            'subSpecies': {
            'val':'',
            'valQuote': eid_pathogen['pathogenSubSpecies'],
            'ref':[],
            'refBlob': eid_pathogen['refPathogenSubSpecies'],
            'meta': meta
            }
        }, #pathogens

        ## Locations
        'locations':{
            'name': {
            'val':'',
            'valQuote': eid_location['locationLocationName'],
            'ref':[],
            'refBlob': eid_location['refLocationLocationName'],
            'meta': meta
            },

            'placeName': {
            'val':'',
            'valQuote': eid_location['locationPlaceName'],
            'ref':[],
            'refBlob': eid_location['refLocationPlaceName'],
            'meta': meta
            },

            'latitude': {
            'val':'',
            'valQuote': eid_location['locationLatitude'],
            'ref':[],
            'refBlob': eid_location['refLocationLatitude'],
            'meta': meta
            },

            'longitude': {
            'val':'',
            'valQuote': eid_location['locationLongitude'],
            'ref':[],
            'refBlob': eid_location['refLocationLongitude'],
            'meta': meta
            },

            'city': {
            'val':'',
            'valQuote': eid_location['locationCity'],
            'ref':[],
            'refBlob': eid_location['refLocationCity'],
            'meta': meta
            },

            'subnationalRegion': {
            'val':'',
            'valQuote': eid_location['locationSubnationalRegion'],
            'ref':[],
            'refBlob': eid_location['refLocationSubnationalRegion'],
            'meta': meta
            },

            'nation': {
            'val':'',
            'valQuote': eid_location['locationNation'],
            'ref':[],
            'refBlob': eid_location['refLocationNation'],
            'meta': meta
            },

            'continent': {
            'val':'',
            'valQuote': eid_location['locationContinent'],
            'ref':[],
            'refBlob': eid_location['refLocationContinent'],
            'meta': meta
            }
        }, #locations

        ## Hosts
        'hosts':{
            'sex': {
            'val':'',
            'valQuote': eid['hostSex'],
            'ref':[],
            'refBlob': eid['refHostSex'],
            'meta': meta
            },

            'domesticationStatus': {
            'val':'',
            'valQuote': eid['domesticationStatus'],
            'ref':[],
            'refBlob': eid['refDomesticationStatus'],
            'meta': meta
            },

            'age': {
            'val':eid['hostAgeVal'],
            'valQuote': eid['hostAge'],
            'ref':[],
            'refBlob': eid['refHostAge'],
            'meta': meta
            },

            'hostUse': {
            'val':'',
            'valQuote': eid['hostUse'],
            'ref':[],
            'refBlob': eid['refHostUse'],
            'meta': meta
            },

            'reportedName': {
            'val':'',
            'valQuote': eid_host['hostReportedName'],
            'ref':[],
            'refBlob': eid_host['refHostReportedName'],
            'meta': meta
            },

            'class': {
            'val':'',
            'valQuote': eid_host['hostClass'],
            'ref':[],
            'refBlob': eid_host['refHostClass'],
            'meta': meta
            },

            'family': {
            'val':'',
            'valQuote': eid_host['hostFamily'],
            'ref':[],
            'refBlob': eid_host['refHostFamily'],
            'meta': meta
            },

            'species': {
            'val':'',
            'valQuote': eid_host['hostSpecies'],
            'ref':[],
            'refBlob': eid_host['refHostSpecies'],
            'meta': meta
            },

            'authority': {
            'val':'',
            'valQuote': eid_host['hostAuthority'],
            'ref':[],
            'refBlob': eid_host['refHostAuthority'],
            'meta': meta
            },

            'taxOrder': {
            'val':'',
            'valQuote': eid_host['hostTaxOrder'],
            'ref':[],
            'refBlob': eid_host['refHostTaxOrder'],
            'meta': meta
            },

            'genus': {
            'val':'',
            'valQuote': eid_host['hostGenus'],
            'ref':[],
            'refBlob': eid_host['refHostGenus'],
            'meta': meta
            },

            'subSpecies': {
            'val':'',
            'valQuote': eid_host['hostSubSpecies'],
            'ref':[],
            'refBlob': eid_host['refHostSubSpecies'],
            'meta': meta
            }
        }, #hosts 
        
        ## Dates
        'dates':{
            'startDate':{
                'val':'',
                'valQuote': eid['startDate'],
                'valForm': eid['startDateISO'],
                'ref':[],
            'refBlob': eid['refStartDate'],
                'meta': meta
            },
            'endDate':{
                'val':'',
                'valQuote': eid['endDate'],
                'valForm': eid['endDateISO'],
                'ref':[],
            'refBlob': eid['refEndDate'],
                'meta': meta
            },
            'duration': {
                'val':'',
                'valQuote': eid['duration'],
                'ref':[],
            'refBlob': eid['refDuration'],
                'meta': meta
            }
        }, #dates

        ## Characteristics
        'characteristics':{
            'numberInfected': {
            'val':eid['numberInfectedVal'],
            'valQuote': eid['numberInfected'],
            'ref':[],
            'refBlob': eid['refNumberInfected'],
            'meta': meta
            },

            'prevalence': {
            'val':'',
            'valQuote': eid['prevalence'],
            'ref':[],
            'refBlob': eid['refPrevalence'],
            'meta': meta
            },

            'symptomsReported': {
            'val':eid['SymptomsReportedVal'],
            'valQuote': eid['symptomsReported'],
            'ref':[],
            'refBlob': eid['refSymptomsReported'],
            'meta': meta
            },

            'numberOfDeaths': {
            'val':eid['numberOfDeathsVal'],
            'valQuote': eid['numberOfDeaths'],
            'ref':[],
            'refBlob': eid['refNumberofDeaths'],
            'meta': meta
            },
        }, #characteristics

        ## Contacts
        'contacts':{
            'firstName': '',
            'lastName': '',
            'email': '',
            'affiliation': '',
            'userID': '',
            'blob': {
                'val': eid['contact'],
                'ref':[],
            'refBlob': eid['refContact']
            },
            'meta': meta
        }, # contacts

        ## Economics
        'economics':{
            'avgAgeInfected': {
            'val':'',
            'valQuote': eid_economics['avgAgeOfInfected'],
            'ref':[],
            'refBlob': eid_economics['refAvgAgeOfInfected'],
            'meta': meta},

            'avgAgeDeath': {
            'val':'',
            'valQuote': eid_economics['avgAgeDeath'],
            'ref':[],
            'refBlob': eid_economics['refAvgAgeDeath'],
            'meta': meta},

            'tradeTravelRestrictions': {
            'val':'',
            'valQuote': eid_economics['tradeTravelRestrictions'],
            'ref':[],
            'refBlob': eid_economics['refTradeTravelRestrictions'],
            'meta': meta},

            'numHospitalized': {
            'val':'',
            'valQuote': eid_economics['numHospitalizedInEvent'],
            'ref':[],
            'refBlob': eid_economics['refNumHospInEvent'],
            'meta': meta},

            'avgCostPerTreatment': {
            'val':'',
            'valQuote': eid_economics['avgCosPerTreatmentInEvent'],
            'ref':[],
            'refBlob': eid_economics['refAvgCostTreatmentInEvent'],
            'meta': meta            
            },

            'perCapitaNatGDPEventYear': {
            'val':'',
            'valQuote': eid_economics['perCapitaNationalGDPInYearOfEvent'],
            'ref':[],
            'refBlob': eid_economics['refPerCapitaNationalGDPInYearOfEvent'],
            'meta': meta
            },

            'avgLifeExpectEventCountryYear': {
            'val':'',
            'valQuote': eid_economics['avgLifeExpectancyInCountryAndYearOfEvent'],
            'ref':[],
            'refBlob': eid_economics['refAvgLifeExpectancyInCountryAndYearOfEvent'],
            'meta': meta
            }
        } # economics
    } # value object

    } #body
    
    #fix the OjectID format
    eid_body['_id'] = str(ObjectId())

    #print eid_body['refs'][0]
    #print count

    #['sickiID']
    #['meta']['reviewer']
    db.entries.insert(eid_body)