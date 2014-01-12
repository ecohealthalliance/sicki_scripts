import pymongo, time

db = pymongo.Connection('localhost', 27017)['sicki2']

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

metaData = {
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
  'submitted': time.time()
}

print metaData


#dates = ['startDate','startDateISO','refStartDate','endDate','endDateISO','refEndDate']

for eid in eid_events:
    #print eid['eventName']

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

        id = eid.get('_id')

        eid_body = {
        'metaData': {
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
          'submitted': time.time()
        },

        'commentsCount': 0, #Calculated field
        'refsCount': 0, #Calculated field
        'refs': [], #Calculated field

        'sickiID':{
        'value': eid['eidID'],
        'ref': 'jones',
        'metaData': metaData
        },



        'eventName':{
        'value': eid['eventName'],
        'ref': 'jones',
        'metaData': metaData
        },

        'disease':{
        'value': eid['disease'],
        'ref': eid['refDisease'],
        'metaData': metaData
        },

        'eid':{
        'value': eid['eid'],
        'ref': eid['refEID'],
        'metaData': metaData
        },

        'eidCategory':{
        'value': eid['eidCategory'],
        'ref': eid['refEIDCategory'],
        'metaData': metaData
        },

        'abstract': {
        'value': eid['Abstract'],
        'ref': eid['refAbstract'],
        'metaData': metaData
        },

        'notes': {
        'value': eid['notes'],
        'ref': eid['refNotes'],
        'metaData': metaData
        },

        'transmissionModel': {
        'value': eid['transitionModel'],
        'ref': eid['refTransitionModel'],
        'metaData': metaData
        },

        'zoonoticType': {
        'value': eid['zoonoticType'],
        'ref': eid['refZoonoticType'],
        'metaData': metaData
        },

        'sampleType': {
        'value': eid['sampleType'],
        'ref': eid['refSampleType'],
        'metaData': metaData
        },

        'driver': {
        'value': eid['driver'],
        'ref': eid['refDriver'],
        'metaData': metaData
        },

        ## Pathogens
        'pathogens':{
            'drugResistance': {
            'value': eid_pathogen['pathogenDrugResistance'],
            'ref': eid_pathogen['refPathogenDrugResistance'],
            'metaData': metaData
            },

            'reportedName': {
            'value': eid_pathogen['pathogenReportedName'],
            'ref': eid_pathogen['refPathogenReportedName'],
            'metaData': metaData
            },

            'class': {
            'value': eid_pathogen['pathogenClass'],
            'ref': eid_pathogen['refPathogenClass'],
            'metaData': metaData
            },

            'family': {
            'value': eid_pathogen['pathogenFamily'],
            'ref': eid_pathogen['refPathogenFamily'],
            'metaData': metaData
            },

            'species': {
            'value': eid_pathogen['pathogenSpecies'],
            'ref': eid_pathogen['refPathogenSpecies'],
            'metaData': metaData
            },

            'authority': {
            'value': eid_pathogen['pathogenAuthority'],
            'ref': eid_pathogen['refPathogenAuthority'],
            'metaData': metaData
            },

            'taxOrder': {
            'value': eid_pathogen['pathogenTaxOrder'],
            'ref': eid_pathogen['refPathogenTaxOrder'],
            'metaData': metaData
            },

            'genus': {
            'value': eid_pathogen['pathogenGenus'],
            'ref': eid_pathogen['refPathogenGenus'],
            'metaData': metaData
            },

            'subSpecies': {
            'value': eid_pathogen['pathogenSubSpecies'],
            'ref': eid_pathogen['refPathogenSubSpecies'],
            'metaData': metaData
            }
        }, #pathogens

        ## Locations
        'locations':{
            'name': {
            'value': eid_location['locationLocationName'],
            'ref': eid_location['refLocationLocationName'],
            'metaData': metaData
            },

            'placeName': {
            'value': eid_location['locationPlaceName'],
            'ref': eid_location['refLocationPlaceName'],
            'metaData': metaData
            },

            'latitude': {
            'value': eid_location['locationLatitude'],
            'ref': eid_location['refLocationLatitude'],
            'metaData': metaData
            },

            'longitude': {
            'value': eid_location['locationLongitude'],
            'ref': eid_location['refLocationLongitude'],
            'metaData': metaData
            },

            'city': {
            'value': eid_location['locationCity'],
            'ref': eid_location['refLocationCity'],
            'metaData': metaData
            },

            'subnationalRegion': {
            'value': eid_location['locationSubnationalRegion'],
            'ref': eid_location['refLocationSubnationalRegion'],
            'metaData': metaData
            },

            'nation': {
            'value': eid_location['locationNation'],
            'ref': eid_location['refLocationNation'],
            'metaData': metaData
            },

            'continent': {
            'value': eid_location['locationContinent'],
            'ref': eid_location['refLocationContinent'],
            'metaData': metaData
            }
        }, #locations

        ## Hosts
        'hosts':{
            'sex': {
            'value': eid['hostSex'],
            'ref': eid['refHostSex'],
            'metaData': metaData
            },

            'domesticationStatus': {
            'value': eid['domesticationStatus'],
            'ref': eid['refDomesticationStatus'],
            'metaData': metaData
            },

            'age': {
            'value': eid['hostAge'],
            'ref': eid['refHostAge'],
            'metaData': metaData
            },

            'hostUse': {
            'value': eid['hostUse'],
            'ref': eid['refHostUse'],
            'metaData': metaData
            },

            'reportedName': {
            'value': eid_host['hostReportedName'],
            'ref': eid_host['refHostReportedName'],
            'metaData': metaData
            },

            'class': {
            'value': eid_host['hostClass'],
            'ref': eid_host['refHostClass'],
            'metaData': metaData
            },

            'family': {
            'value': eid_host['hostFamily'],
            'ref': eid_host['refHostFamily'],
            'metaData': metaData
            },

            'species': {
            'value': eid_host['hostSpecies'],
            'ref': eid_host['refHostSpecies'],
            'metaData': metaData
            },

            'authority': {
            'value': eid_host['hostAuthority'],
            'ref': eid_host['refHostAuthority'],
            'metaData': metaData
            },

            'taxOrder': {
            'value': eid_host['hostTaxOrder'],
            'ref': eid_host['refHostTaxOrder'],
            'metaData': metaData
            },

            'genus': {
            'value': eid_host['hostGenus'],
            'ref': eid_host['refHostGenus'],
            'metaData': metaData
            },

            'subSpecies': {
            'value': eid_host['hostSubSpecies'],
            'ref': eid_host['refHostSubSpecies'],
            'metaData': metaData
            }
        }, #hosts 
        
        ## Dates
        'dates':{
            'startDate':{
                'value': eid['startDate'],
                'formValue': eid['startDateISO'],
                'ref': eid['refStartDate'],
                'metaData': metaData
            },
            'endDate':{
                'value': eid['endDate'],
                'formValue': eid['endDateISO'],
                'ref': eid['refEndDate'],
                'metaData': metaData
            },
            'duration': {
                'value': eid['duration'],
                'ref': eid['refDuration'],
                'metaData': metaData
            }
        }, #dates

        ## Characteristics
        'characteristics':{
            'numberInfected': {
            'value': eid['numberInfected'],
            'ref': eid['refNumberInfected'],
            'metaData': metaData
            },

            'prevalence': {
            'value': eid['prevalence'],
            'ref': eid['refPrevalence'],
            'metaData': metaData
            },

            'symptomsReported': {
            'value': eid['symptomsReported'],
            'ref': eid['refSymptomsReported'],
            'metaData': metaData
            },

            'numberOfDeaths': {
            'value': eid['numberOfDeaths'],
            'ref': eid['refNumberofDeaths'],
            'metaData': metaData
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
                'value': eid['contact'],
                'ref': eid['refContact']
            },
            'metaData': metaData
        }, # contacts

        ## Economics
        'economics':{
            'avgAgeInfected': {
            'value': eid_economics['avgAgeOfInfected'],
            'ref': eid_economics['refAvgAgeOfInfected'],
            'metaData': metaData},

            'avgAgeDeath': {
            'value': eid_economics['avgAgeDeath'],
            'ref': eid_economics['refAvgAgeDeath'],
            'metaData': metaData},

            'tradeTravelRestrictions': {
            'value': eid_economics['tradeTravelRestrictions'],
            'ref': eid_economics['refTradeTravelRestrictions'],
            'metaData': metaData},

            'numHospitalized': {
            'value': eid_economics['numHospitalizedInEvent'],
            'ref': eid_economics['refNumHospInEvent'],
            'metaData': metaData},

            'avgCostPerTreatment': {
            'value': eid_economics['avgCosPerTreatmentInEvent'],
            'ref': eid_economics['refAvgCostTreatmentInEvent'],
            'metaData': metaData            
            },

            'perCapitaNatGDPEventYear': {
            'value': eid_economics['perCapitaNationalGDPInYearOfEvent'],
            'ref': eid_economics['refPerCapitaNationalGDPInYearOfEvent'],
            'metaData': metaData
            },

            'avgLifeExpectEventCountryYear': {
            'value': eid_economics['avgLifeExpectancyInCountryAndYearOfEvent'],
            'ref': eid_economics['refAvgLifeExpectancyInCountryAndYearOfEvent'],
            'metaData': metaData
            }
        } # economics

        } #body
    #print eid_body['sickiID']['metaData']['reviewer']
    db.entry.insert(eid_body)