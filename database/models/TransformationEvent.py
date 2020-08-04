# -*- coding: utf-8 -*-

#import packages
import mongoengine as odm
import numpy as np
import datetime

#import dependences
from database.models.Event import event 
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
    quantity = odm.FloatField() #The quantity of objects with the class (i.e. specific packaging unit) described by this event
    
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
def defineTranformationEvent(physicalGood_input,
                             physicalGood_output,
                             epcClass=None,
                             xformID=None,
                             quantity=np.nan,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={}):
    
    document={}
    
    '''
    #why
    disposition = odm.StringField() #The business state of an object such as sold, expired, recalled, in transit
    bizStep = odm.StringField() #The business step of which EPCIS event was a part
    bizTransactionList = odm.ListField() #A list of business transaction that defines the context of the event {bizTransactionType, bizTransaction}
    
    
    sourceDestList = odm.ListField() #A list of business transfer that defines the additional context of the EPCIS event {SourceDestType, SourceDest}
    ilmd = odm.StringField() #A specific instance of a physical or digital object
    extensions = odm.ListField() #This identifies the addition of new data members, list of additional attributes

    '''
    
    
    #set object parameters
    document['eventTime'] = datetime.datetime.utcnow()
    document['recordTime'] = datetime.datetime.utcnow()
    
        
    #what
    #each event involves a single epc        
    document['inputEpc'] = physicalGood_input.epc
    document['outputEpc'] = physicalGood_output.epc
    document['epcClass'] = epcClass 
    document['xformID'] = xformID
    document['quantity'] = quantity
    
    
    
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
    
    
    
    document['extensions'] = extensions
    
    return document

# %%

def ADDtransformationEvent(physicalGood_input,
                             physicalGood_output,
                             epcClass=None,
                             xformID=None,
                             quantity=np.nan,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    
    document = defineTranformationEvent(physicalGood_input=physicalGood_input,
                             physicalGood_output=physicalGood_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity=quantity,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions=extensions)
    
    document['action'] = "ADD"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['TransformationEvent'].insert_one(document)
    
    return result

# %%

def OBSERVEtransformationEvent(physicalGood_input,
                             physicalGood_output,
                             epcClass=None,
                             xformID=None,
                             quantity=np.nan,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    
    document = defineTranformationEvent(physicalGood_input=physicalGood_input,
                             physicalGood_output=physicalGood_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity=quantity,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions=extensions)
    
    document['action'] = "OBSERVE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['TransformationEvent'].insert_one(document)
    
    return result

# %%

def DELETEtransformationEvent(physicalGood_input,
                             physicalGood_output,
                             epcClass=None,
                             xformID=None,
                             quantity=np.nan,
                             nodeDict=None,
                             disposition=None,
                             bizStep=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    
    document = defineTranformationEvent(physicalGood_input=physicalGood_input,
                             physicalGood_output=physicalGood_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity=quantity,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions=extensions)
    
    document['action'] = "DELETE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['TransformationEvent'].insert_one(document)
    
    return result

