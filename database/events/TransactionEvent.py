# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#import packages
import mongoengine as odm
import datetime

#import dependences
from database.events.Event import event 
import database.mongo_loginManager as mdb


# %% class objectEvent model
class TransactionEvent(event):
    #when
    eventTime = odm.DateTimeField(required=True) #The date and time at which the event occurred
    recordTime = odm.DateTimeField() #The date and time at which event was recorded by an EPCIS repository
    
    #what
    eventID = odm.ObjectIdField(primary_key=True, required=True) #A globally unique identifier across all the events
        #physical entity
    epcList = odm.ListField() #A list of observed EPCs naming the physical objects
    parentID = odm.StringField() #The identifier of the parent of the association (container)
    
    action = odm.StringField(required=True) #How an event relates to the lifecycle of the entity being described {ADD, OBSERVE, DELETE}
    
    #quantity
    quantity = odm.FloatField(required=True) #The quantity of objects with the class (i.e. specific packaging unit) described by this event
    quantity_udm = odm.StringField() #Unit of measure of the quantity
        
   
    #where
    readPoint = odm.StringField() #The specific location at which EPCIS event took place
    bizLocation = odm.StringField() #The business location where an object is following an EPCIS event
    
    #why
    disposition = odm.StringField() #The business state of an object such as sold, expired, recalled, in transit
    bizStep = odm.StringField() #The business step of which EPCIS event was a part
    bizTransactionList = odm.ListField(required=True) #A list of business transaction that defines the context of the event {bizTransactionType, bizTransaction}
    sourceDestList = odm.ListField(required=True) #A list of business transfer that defines the additional context of the EPCIS event {SourceDestType, SourceDest}
    extensions = odm.ListField() #This identifies the addition of new data members, list of additional attributes

# %%
def defineTransactionEvent(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   bizTransactionList,
                   DestnodeDict,
                   bizStep=None,
                   parentID=[],
                   disposition=None,
                   extensions={}):
    
    document={}
    
    
    #set object parameters
    document['eventTime'] = datetime.datetime.utcnow()
    document['recordTime'] = datetime.datetime.utcnow()
    
        
    #what
    #each event involves a single epc        
    document['epc'] = physicalGoodDict.epc
    document['parentID'] = parentID
    
    document['quantity'] = quantity
    document['quantity_udm'] = quantity_udm
    
    #where
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
    
    document['Dest_net'] = DestnodeDict['nodeNet']
    document['Dest_Type'] = DestnodeDict['nodeType']
    document['Dest'] = DestnodeDict['nodeName']
    document['Dest_geo_lat'] = DestnodeDict['geo_position'][0]
    document['Dest_geo_lon'] = DestnodeDict['geo_position'][1]
    document['Dest_plant_x'] = DestnodeDict['plant_position'][0]
    document['Dest_plant_y'] = DestnodeDict['plant_position'][1]
    document['Dest_plant_z'] = DestnodeDict['plant_position'][2]
    
    document['extensions'] = extensions
    
    return document
# %%

def ADDtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=None,
                   parentID=[],
                   disposition=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    
    document = defineTransactionEvent(physicalGoodDict= physicalGoodDict,
                   nodeDict=nodeDict,
                   bizTransactionList=bizTransactionList,
                   DestnodeDict=DestnodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   bizStep=bizStep,
                   parentID=parentID,
                   disposition=disposition,
                   extensions=extensions)
    
    document['action'] = "ADD"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['TransactionEvent'].insert_one(document)
    
    return result

# %%
def OBSERVEtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=None,
                   parentID=[],
                   disposition=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    
    document = defineTransactionEvent(physicalGoodDict= physicalGoodDict,
                   nodeDict=nodeDict,
                   bizTransactionList=bizTransactionList,
                   DestnodeDict=DestnodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   bizStep=bizStep,
                   parentID=parentID,
                   disposition=disposition,
                   extensions=extensions)
    
    document['action'] = "OBSERVE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['TransactionEvent'].insert_one(document)
    
    return result

# %%
def DELETEtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=None,
                   parentID=[],
                   disposition=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    
    document = defineTransactionEvent(physicalGoodDict= physicalGoodDict,
                   nodeDict=nodeDict,
                   bizTransactionList=bizTransactionList,
                   DestnodeDict=DestnodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   bizStep=bizStep,
                   parentID=parentID,
                   disposition=disposition,
                   extensions=extensions)
    
    document['action'] = "DELETE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    result = db['TransactionEvent'].insert_one(document)
    
    return result

