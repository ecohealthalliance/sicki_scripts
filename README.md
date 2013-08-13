# GH/ecohealthalliance/sicki_scripts

The goal of these scripts is to ensure we can reproduce any modifications we make to the original data (spreadsheets) by rerunning the scripts (goal = reproducibility). The spreadsheets were uploaded to mongodb as collections, then the scripts were run to generate the events collection.

## Source spreadsheets:

1. match-key.csv  
 Jones et al. Supplemental Appendix - prepared by Nico  
 n = 333  

2. CCM_EIDDatabase_041005  
 EHA Internal Spreadsheet - prepared by Carlos/Nico & predecessors  
 n = 475  

## Steps
1. Load original dataset
    python orig.py CCM_EIDDatabase_041005.csv
This will create the database eids and the collection orig_events
2. Create the initial field names
    python init_move.py

X. Add data from the Jones Supplementary info
   
## Sicki Scripts:

### add_accepted_date_tp_ref_proposals.py  
what: accepted dates to proposals for original zotero references  
from: proposal  
to: proposal  

### add_centroid.py
what: centroid of geojson objects  
from: centroid calculated from Maps_Projected/maps  
to: events.centroid  

### add_refs.py
what: blank list of ref ids  
from: [ ]  
to: events.references  
  
### add_shp.py  
what: reference to a shape file  
from: item['FileName'].replace ('.shp', '')  
to: events.map  
  
### clear_refs.py  
what: clear the references entries to repopulate  
from: [ ] &  orig_events['_id']  
to: events.references & events.orig_event  
  
### disease.py  
what: update the disease name  
from:  orig_events.Path_DName  
to: events.disease  
  
### eid_id.py  
what: create an eid_id field from the hed_id (geospatial id), remove “hed”  
from: events.map  
to: events.eid_id  
  
### init_move.py  
what: create a unique title field for referencing events  
from: join of ‘PathEmerge_Date_Yr’, ‘PathEmerge_Location’, ‘Path_BNSpp'  
to: events.event_name  
  
### jones2mongo.py  
what: join on field eid_id and import all of match_key as json object in field ‘jones’  
from: /Dropbox/sicki/match-key.csv
to: events.jones  
  
### location.py  
what: set the original location  
from: events_orig.PathEmerge_Location  
to: events.location  
  
### make_pathogens_singular.py  
what: rename pathogens field to pathogen  
from: eid  
to: eid  

### match_refs.py   
what: match references list on the rights field then adds the zotero_id  
 perhaps also with match_key.csv  
from: refs.rights  
to: events.references  
  
### merge_asc.py  
what: add the ascii file to the events, this is for the overview of all events map  
from: sicki_maps/merge.asc  
to: maps.geodata  
  
### merge_geodata.py   
what: add geojson to the events, this is for the individual events maps  
from: ../sicki_maps/file.json  
to: maps.geodata  

### move_fields_to_proposals.py  
what: move fields from eid collection to proposals and make the fields arrays of proposal references  
from: eid  
to: eid, proposal  

### move_refs_to_proposals.py  
what: move fields from reference collection to proposals and make the fields arrays of proposal ids  
from: reference  
to: reference, proposal  

### non_mongo_proposal_ids.py  
what: convert mongo object ids to hex for proposals  
from: eid, proposal  
to:  eid, proposal
  
### orig.py  
what: loads data from original csv file  
from: CCM_EIDDatabase_041005  
to: orig_events  
  
### pathogen.py  
what: matches pathogen name   
from: orig_events.Path_BNGenus, Path_BNSpp, Path_CName  
to: events.pathogens.genus, species, reported_name  
  
### plural.py  
what: makes collection name plural  
from: event  
to: events  
  
### pre_pop_wiki.py  
what: enters dummy text  
from: Lorem Ipsum  
to: events.body  
  
### pull_refs.py  
what: imports eids data from Zotero to mongo  
from: library_id = 126319 https://www.zotero.org/groups/126319  
to: refs  
  
### rename.py  
what: build custom naming convention  
from: events_orig.Path_BNGenus+Path_BNSpp or Path_CName & PathEmerge_Date_Yr & PathEmerge_Location  
to : events.event_name  
  
### re_host.py  
what: assign host name  
from: events_orig.Path_ResHost  
to: events.host  
  
### start_date.py  
what: maps start date  
from: orig_event.PathEmerge_Date  
to: events.start_date  
  
### zotero.py  
what: inserts Zotero references in Mongo  
from: library 77783  
to: refs  
