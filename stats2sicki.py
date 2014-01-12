import pymongo, time

db = pymongo.Connection('localhost', 27017)['sicki2']

# source collections
#economics = db.economics
event = db.event
#host = db.host
#location = db.location
#meta = db.meta
#metrics = db.metrics
#pathogen = db.pathogen

# update entries from the other collections
eid_events = event.find()

#dates = ['startDate','startDateISO','refStartDate','endDate','endDateISO','refEndDate']

for eid in eid_events:
    print eid['eventName']

    # Load host
    cursor = db.host.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_host = value
        print eid_host['hostTaxOrder']

    # Load economics
    cursor = db.economics.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_economics = value
        print eid_economics['avgAgeDeath']

    # Load pathogens
    cursor = db.pathogen.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_pathogen = value
        print eid_pathogen['pathogenClass']

    # Load locations
    cursor = db.location.find ({'eventName': eid['eventName']})
    for value in cursor:
        eid_location = value
        print eid_location['locationNation']

        id = eid.get('_id')
        eid_body = {
        'eidID': eid['eidID'],
        'eventName': eid['eventName'],
        'disease':{
        'value': eid['disease'],
        'ref': eid['refDisease'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
        'userId': 1,
        'author': eid['reviewer'],
        'submitted': time.time()
        },
        'eid':{
        'value': eid['eid'],
        'ref': eid['refEID'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'eidCategory':{
        'value': eid['eidCategory'],
        'ref': eid['refEIDCategory'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'abstract': {
        'value': eid['Abstract'],
        'ref': eid['refAbstract'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'notes': {
        'value': eid['notes'],
        'ref': eid['refNotes'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'transmissionModel': {
        'value': eid['transitionModel'],
        'ref': eid['refTransitionModel'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'zoonoticType': {
        'value': eid['zoonoticType'],
        'ref': eid['refZoonoticType'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'sampleType': {
        'value': eid['sampleType'],
        'ref': eid['refSampleType'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        'driver': {
        'value': eid['driver'],
        'ref': eid['refDriver'],
        'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        },

        ## Pathogens
        'pathogens':{
            'drugResistance': {
            'value': eid_pathogen['pathogenDrugResistance'],
            'ref': eid_pathogen['refPathogenDrugResistance'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'reportedName': {
            'value': eid_pathogen['pathogenReportedName'],
            'ref': eid_pathogen['refPathogenReportedName'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'class': {
            'value': eid_pathogen['pathogenClass'],
            'ref': eid_pathogen['refPathogenClass'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'family': {
            'value': eid_pathogen['pathogenFamily'],
            'ref': eid_pathogen['refPathogenFamily'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'species': {
            'value': eid_pathogen['pathogenSpecies'],
            'ref': eid_pathogen['refPathogenSpecies'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'authority': {
            'value': eid_pathogen['pathogenAuthority'],
            'ref': eid_pathogen['refPathogenAuthority'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'taxOrder': {
            'value': eid_pathogen['pathogenTaxOrder'],
            'ref': eid_pathogen['refPathogenTaxOrder'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'genus': {
            'value': eid_pathogen['pathogenGenus'],
            'ref': eid_pathogen['refPathogenGenus'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'subSpecies': {
            'value': eid_pathogen['pathogenSubSpecies'],
            'ref': eid_pathogen['refPathogenSubSpecies'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            }
        }, #pathogens

        ## Locations
        'locations':{
            'name': {
            'value': eid_location['locationLocationName'],
            'ref': eid_location['refLocationLocationName'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'placeName': {
            'value': eid_location['locationPlaceName'],
            'ref': eid_location['refLocationPlaceName'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'latitude': {
            'value': eid_location['locationLatitude'],
            'ref': eid_location['refLocationLatitude'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'longitude': {
            'value': eid_location['locationLongitude'],
            'ref': eid_location['refLocationLongitude'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'city': {
            'value': eid_location['locationCity'],
            'ref': eid_location['refLocationCity'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'subnationalRegion': {
            'value': eid_location['locationSubnationalRegion'],
            'ref': eid_location['refLocationSubnationalRegion'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'nation': {
            'value': eid_location['locationNation'],
            'ref': eid_location['refLocationNation'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'continent': {
            'value': eid_location['locationContinent'],
            'ref': eid_location['refLocationContinent'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            }
        }, #locations

        ## Hosts
        'hosts':{
            'sex': {
            'value': eid['hostSex'],
            'ref': eid['refHostSex'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'domesticationStatus': {
            'value': eid['domesticationStatus'],
            'ref': eid['refDomesticationStatus'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'age': {
            'value': eid['hostAge'],
            'ref': eid['refHostAge'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'hostUse': {
            'value': eid['hostUse'],
            'ref': eid['refHostUse'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'reportedName': {
            'value': eid_host['hostReportedName'],
            'ref': eid_host['refHostReportedName'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'class': {
            'value': eid_host['hostClass'],
            'ref': eid_host['refHostClass'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'family': {
            'value': eid_host['hostFamily'],
            'ref': eid_host['refHostFamily'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'species': {
            'value': eid_host['hostSpecies'],
            'ref': eid_host['refHostSpecies'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'authority': {
            'value': eid_host['hostAuthority'],
            'ref': eid_host['refHostAuthority'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'taxOrder': {
            'value': eid_host['hostTaxOrder'],
            'ref': eid_host['refHostTaxOrder'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'genus': {
            'value': eid_host['hostGenus'],
            'ref': eid_host['refHostGenus'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'subSpecies': {
            'value': eid_host['hostSubSpecies'],
            'ref': eid_host['refHostSubSpecies'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            }
        }, #hosts 
        
        ## Dates
        'dates':{
            'startDate':{
                'value': eid['startDate'],
                'formValue': eid['startDateISO'],
                'ref': eid['refStartDate'],
                'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },
            'endDate':{
                'value': eid['endDate'],
                'formValue': eid['endDateISO'],
                'ref': eid['refEndDate'],
                'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },
            'duration': {
                'value': eid['duration'],
                'ref': eid['refDuration'],
                'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            }
        }, #dates

        ## Characteristics
        'characteristics':{
            'numberInfected': {
            'value': eid['numberInfected'],
            'ref': eid['refNumberInfected'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'prevalence': {
            'value': eid['prevalence'],
            'ref': eid['refPrevalence'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'symptomsReported': {
            'value': eid['symptomsReported'],
            'ref': eid['refSymptomsReported'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'numberOfDeaths': {
            'value': eid['numberOfDeaths'],
            'ref': eid['refNumberofDeaths'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
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
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
        }, # contacts

        ## Economics
        'economics':{
            'avgAgeInfected': {
            'value': eid_economics['avgAgeOfInfected'],
            'ref': eid_economics['refAvgAgeOfInfected'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()},

            'avgAgeDeath': {
            'value': eid_economics['avgAgeDeath'],
            'ref': eid_economics['refAvgAgeDeath'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()},

            'tradeTravelRestrictions': {
            'value': eid_economics['tradeTravelRestrictions'],
            'ref': eid_economics['refTradeTravelRestrictions'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()},

            'numHospitalized': {
            'value': eid_economics['numHospitalizedInEvent'],
            'ref': eid_economics['refNumHospInEvent'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()},

            'avgCostPerTreatment': {
            'value': eid_economics['avgCosPerTreatmentInEvent'],
            'ref': eid_economics['refAvgCostTreatmentInEvent'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()            
            },

            'perCapitaNatGDPEventYear': {
            'value': eid_economics['perCapitaNationalGDPInYearOfEvent'],
            'ref': eid_economics['refPerCapitaNationalGDPInYearOfEvent'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            },

            'avgLifeExpectEventCountryYear': {
            'value': eid_economics['avgLifeExpectancyInCountryAndYearOfEvent'],
            'ref': eid_economics['refAvgLifeExpectancyInCountryAndYearOfEvent'],
            'rank':{
                'eha':True,
                'upvotes':0,
                'downvotes':0,
                },
            'userId': 1,
            'author': eid['reviewer'],
            'submitted': time.time()
            }
        }, # economics

        'rank':{
            'eha':True
            },
        'upvotes':0,
        'downvotes':0,
        'userId': 1,
        'author': eid['reviewer'],
        'submitted': time.time(),
        'commentsCount': 0
        } #body
    print eid_body['contacts']['blob']
    db.entry.insert(eid_body)