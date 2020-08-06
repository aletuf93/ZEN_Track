# -*- coding: utf-8 -*-

#import packages
import mongoengine as odm
import numpy as np
import datetime

#import dependences
from database.events.Event import event 
from database.entities.physicalGood_class import physicalGood_class
import database.mongo_loginManager as mdb


# %% DEFINE THE EVENT CLASS
class TransformationEvent(event):
        
    #when
    eventTime = odm.DateTimeField(required=True) #The date and time at which the event occurred
    recordTime = odm.DateTimeField() #The date and time at which event was recorded by an EPCIS repository
    
    #what
    eventID = odm.ObjectIdField(primary_key=True, required=True) #A globally unique identifier across all the events
        #physical entity
    inputEpc = odm.ListField(required=True) #A list of observed EPCs naming the physical objects
    outputEpc = odm.ListField(required=True)
    epcClass = odm.StringField() #The identifier specifying the object class to which it belongs
       #action
    action = odm.StringField(required=True) #How an event relates to the lifecycle of the entity being described {ADD, OBSERVE, DELETE}
        #resource
    xformID = odm.StringField() # (URN identifier) An identifier for the transformation that compiles with the requirement of uniform resource name (URN) syntax
        #quantity
    quantity_input = odm.FloatField() #The quantity of objects with the class (i.e. specific packaging unit) described by this event
    quantity__input_udm = odm.StringField() #Unit of measure of the quantity
    
    quantity_output = odm.FloatField() #The quantity of objects with the class (i.e. specific packaging unit) described by this event
    quantity__output_udm = odm.StringField() #Unit of measure of the quantity
    
    #where
    readPoint = odm.StringField() #The specific location at which EPCIS event took place
    bizLocation = odm.StringField() #The business location where an object is following an EPCIS event
    
    #why
    disposition = odm.StringField() #The business state of an object such as sold, expired, recalled, in transit
    bizStep = odm.StringField() #The business step of which EPCIS event was a part
    bizTransactionList = odm.ListField() #A list of business transaction that defines the context of the event {bizTransactionType, bizTransaction}
    
    
    sourceDestList = odm.ListField() #A list of business transfer that defines the additional context of the EPCIS event {SourceDestType, SourceDest}
    ilmd = odm.StringField() #A specific instance of a physical or digital object
    extensions = odm.ListField() #This identifies the addition of new data members, list of additional attributes

    
# %%
def defineTranformationEvent(physicalGoodDict_input,
                             physicalGoodDict_output,
                             epcClass=None,
                             xformID=None,
                             quantity_in=np.nan,
                             quantity_in_udm=None,
                             quantity_out=np.nan,
                             quantity_out_udm=None,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={}):
    
    document={}
    
    
    #set object parameters
    document['eventTime'] = datetime.datetime.utcnow()
    document['recordTime'] = datetime.datetime.utcnow()
    
        
    #what
    #each event involves a single epc        
    document['inputEpc'] = physicalGoodDict_input['epc']
    document['outputEpc'] = physicalGoodDict_output['epc']
    document['epcClass'] = epcClass 
    document['xformID'] = xformID
    document['quantity_in'] = quantity_in
    document['quantity_in_udm'] = quantity_in_udm
    document['quantity_out'] = quantity_out
    document['quantity_out_udm'] = quantity_out_udm
    
    
    
    #where
    if isinstance(nodeDict,dict):
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
    
    #add all the other data
    for key in physicalGoodDict_input:
        if key not in document.keys():
            if isinstance(physicalGoodDict_input[key],physicalGood_class):
                document[f"input_{key}"] = physicalGoodDict_input[key].__dict__
            else:
                document[f"input_{key}"] = physicalGoodDict_input[key]
    
    for key in physicalGoodDict_output:
        if key not in document.keys():
            if isinstance(physicalGoodDict_output[key],physicalGood_class):
                document[f"output_{key}"] = physicalGoodDict_output[key].__dict__
            else:
                document[f"output_{key}"] = physicalGoodDict_output[key]
    
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

def ADDtransformationEvent(physicalGoodDict_input,
                             physicalGoodDict_output,
                             epcClass=None,
                             xformID=None,
                             quantity_in=1,
                             quantity_in_udm=None,
                             quantity_out=1,
                             quantity_out_udm=None,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    results = {}
    
    document = defineTranformationEvent(physicalGoodDict_input=physicalGoodDict_input,
                             physicalGoodDict_output=physicalGoodDict_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity_in=quantity_in,
                             quantity_in_udm=quantity_in_udm,
                             quantity_out=quantity_out,
                             quantity_out_udm=quantity_out_udm,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions=extensions)
    
    document['action'] = "ADD"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    results['insert'] = db['TransformationEvent'].insert_one(document)
    
    # update the traceability
    results['track'] = db['PhysicalGood'].update_one({'_id': document['inputEpc']}, {'$push': {'traceability': document}})
    results['track'] = db['PhysicalGood'].update_one({'_id': document['outputEpc']}, {'$push': {'traceability': document}})
    
    return results

# %%

def OBSERVEtransformationEvent(physicalGoodDict_input,
                             physicalGoodDict_output,
                             epcClass=None,
                             xformID=None,
                             quantity_in=1,
                             quantity_in_udm=None,
                             quantity_out=1,
                             quantity_out_udm=None,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    results = {}
    
    document = defineTranformationEvent(physicalGoodDict_input=physicalGoodDict_input,
                             physicalGoodDict_output=physicalGoodDict_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity_in=quantity_in,
                             quantity_in_udm=quantity_in_udm,
                             quantity_out=quantity_out,
                             quantity_out_udm=quantity_out_udm,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions=extensions)
    
    document['action'] = "OBSERVE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    results['insert'] = db['TransformationEvent'].insert_one(document)
    
    # update the traceability
    results['track'] = db['PhysicalGood'].update_one({'_id': document['inputEpc']}, {'$push': {'traceability': document}})
    results['track'] = db['PhysicalGood'].update_one({'_id': document['outputEpc']}, {'$push': {'traceability': document}})
    
    return results

# %%

def DELETEtransformationEvent(physicalGoodDict_input,
                             physicalGoodDict_output,
                             epcClass=None,
                             xformID=None,
                             quantity_in=1,
                             quantity_in_udm=None,
                             quantity_out=1,
                             quantity_out_udm=None,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    results = {}
    
    document = defineTranformationEvent(physicalGoodDict_input=physicalGoodDict_input,
                             physicalGoodDict_output=physicalGoodDict_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity_in=quantity_in,
                             quantity_in_udm=quantity_in_udm,
                             quantity_out=quantity_out,
                             quantity_out_udm=quantity_out_udm,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions=extensions)
    
    document['action'] = "DELETE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    results['insert'] = db['TransformationEvent'].insert_one(document)
    
    # update the traceability
    results['track'] = db['PhysicalGood'].update_one({'_id': document['inputEpc']}, {'$push': {'traceability': document}})
    results['track'] = db['PhysicalGood'].update_one({'_id': document['outputEpc']}, {'$push': {'traceability': document}})
    
    
    return results

