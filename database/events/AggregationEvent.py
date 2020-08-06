# -*- coding: utf-8 -*-
#import packages
import mongoengine as odm
import datetime

#import dependences
from database.entities.physicalGood_class import physicalGood_class
from database.events.Event import event 
import database.mongo_loginManager as mdb


# %% class objectEvent model
class AggregationEvent(event):
    #when
    eventTime = odm.DateTimeField(required=True) #The date and time at which the event occurred
    recordTime = odm.DateTimeField() #The date and time at which event was recorded by an EPCIS repository
    
    #what
    eventID = odm.ObjectIdField(primary_key=True, required=True) #A globally unique identifier across all the events
        #physical entity
    parentID = odm.StringField() #The identifier of the parent of the association (container)
    childEPCs = odm.ListField(required = True) #An unordered list of the EPCs of contained objects (contained)
        #action
    action = odm.StringField(required=True) #How an event relates to the lifecycle of the entity being described {ADD, OBSERVE, DELETE}
        #resource
   
    #where
    readPoint = odm.StringField() #The specific location at which EPCIS event took place
    bizLocation = odm.StringField() #The business location where an object is following an EPCIS event
    
    #why
    disposition = odm.StringField() #The business state of an object such as sold, expired, recalled, in transit
    bizStep = odm.StringField() #The business step of which EPCIS event was a part
    bizTransactionList = odm.ListField() #A list of business transaction that defines the context of the event {bizTransactionType, bizTransaction}
    
    
    sourceDestList = odm.ListField() #A list of business transfer that defines the additional context of the EPCIS event {SourceDestType, SourceDest}
    extensions = odm.ListField() #This identifies the addition of new data members, list of additional attributes

# %%    
def defineAggregationEvent(physicalGoodDict_parent,
                           physicalGoodDict_child,
                           nodeDict=None,
                           disposition=None,
                           bizTransactionList = None,
                           bizStep=None,
                           sourceDestList=None,
                           extensions={}):
    
    document={}
        
    #set object parameters
    document['eventTime'] = datetime.datetime.utcnow()
    document['recordTime'] = datetime.datetime.utcnow()
    
        
    #what
    #each event involves a single epc        
    document['parentID'] = physicalGoodDict_parent['epc']
    document['childEPCs'] = physicalGoodDict_child['epc']
    
    
    #where
    if isinstance(nodeDict, dict):
        document['readPoint_net'] = nodeDict['nodeNet']
        document['readPoint_Type'] = nodeDict['nodeType']
        document['readPoint'] = nodeDict['nodeName']
        document['bizLocation_geo_lat'] = nodeDict['geo_position'][0]
        document['bizLocation_geo_lon'] = nodeDict['geo_position'][1]
        document['bizLocation_plant_x'] = nodeDict['plant_position'][0]
        document['bizLocation_plant_y'] = nodeDict['plant_position'][1]
        document['bizLocation_plant_z'] = nodeDict['plant_position'][2]
    
    #why
    document['disposition'] = disposition
    document['bizStep'] = bizStep
    document['bizTransactionList'] = bizTransactionList
    
    
    document['sourceDestList'] = sourceDestList
    document['extensions'] = extensions
    
    #add all the other data
    for key in physicalGoodDict_parent:
        if key not in document.keys():
            if isinstance(physicalGoodDict_parent[key],physicalGood_class):
                document[f"parent_{key}"] = physicalGoodDict_parent[key].__dict__
            else:
                document[f"parent_{key}"] = physicalGoodDict_parent[key]
    
    for key in physicalGoodDict_child:
        if key not in document.keys():
            if isinstance(physicalGoodDict_child[key],physicalGood_class):
                document[f"child_{key}"] = physicalGoodDict_child[key].__dict__
            else:
                document[f"child_{key}"] = physicalGoodDict_child[key]
    
    for key in extensions:
        if key not in document.keys():
            document[key] = extensions[key]
    
    #unpack values containing dictionaries
    for key in list(document.keys()):
        if isinstance(document[key],dict):
            for key_child in document[key]:
                document[f"{key}_{key_child}"] = document[key][key_child]
            document.pop(key)
    
    return document

# %%
def ADDaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=None,
                    disposition=None,
                    bizTransactionList = None,
                    bizStep=None,
                    sourceDestList=None,
                    extensions={},
                    dbname="EPCIS_DB"):
    
    document = defineAggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=nodeDict,
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions)
    
    document['action'] = "ADD"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['AggregationEvent'].insert_one(document)
    
    return result

# %%
def OBSERVEaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=None,
                    disposition=None,
                    bizTransactionList = None,
                    bizStep=None,
                    sourceDestList=None,
                    extensions={},
                    dbname="EPCIS_DB"):
    
    document = defineAggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=nodeDict,
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions)
    
    document['action'] = "OBSERVE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['AggregationEvent'].insert_one(document)
    
    return result

# %%
def DELETEaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=None,
                    disposition=None,
                    bizTransactionList = None,
                    bizStep=None,
                    sourceDestList=None,
                    extensions={},
                    dbname="EPCIS_DB"):
    
    document = defineAggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=nodeDict,
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions)
    
    document['action'] = "DELETE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['AggregationEvent'].insert_one(document)
    
    return result