#import packages
import mongoengine as odm
import datetime
import numpy as np

#import dependences
from database.entities.physicalGood_class import physicalGood_class
from database.events.Event import event 
from database.inventory.inventory import addInventory, deleteInventory
import database.mongo_loginManager as mdb

# %% class objectEvent model
class ObjectEvent(event):
    #when
    eventTime = odm.DateTimeField(required=True) #The date and time at which the event occurred
    recordTime = odm.DateTimeField() #The date and time at which event was recorded by an EPCIS repository
    
    #what
    eventID = odm.ObjectIdField(primary_key=True, required=True) #A globally unique identifier across all the events
        #physical entity
    epcList = odm.ListField() #A list of observed EPCs naming the physical objects
    
    action = odm.StringField() #How an event relates to the lifecycle of the entity being described {ADD, OBSERVE, DELETE}
        #quantity
    quantity = odm.FloatField(required=True) #The quantity of objects with the class (i.e. specific packaging unit) described by this event
    quantity_udm = odm.StringField() #Unit of measure of the quantity
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
def defineObjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity=np.nan,
                   quantity_udm=None,
                   disposition=None,
                   bizTransactionList = None,
                   bizStep=None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={}):
    
    document={}
    
    #set object parameters
    document['eventTime'] = datetime.datetime.utcnow()
    document['recordTime'] = datetime.datetime.utcnow()
    
        
    #what
    #each event involves a single epc        
    document['epc'] = physicalGoodDict['epc']
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
    
    
    document['sourceDestList'] = sourceDestList
    document['ilmd'] = ilmd
    
    #add all the other data
    for key in physicalGoodDict:
        if key not in document.keys():
            if isinstance(physicalGoodDict[key],physicalGood_class):
                document[f"{key}"] = physicalGoodDict[key].__dict__
            else:
                document[f"{key}"] = physicalGoodDict[key]
    
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
    




def ADDobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition=None,
                   bizTransactionList = None,
                   bizStep=None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    results = {}
    document = defineObjectEvent(physicalGoodDict=physicalGoodDict,
                   nodeDict=nodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=sourceDestList,
                   ilmd=ilmd,
                   extensions=extensions)
    
    document['action'] = "ADD"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    results['insert'] = db['ObjectEvent'].insert_one(document)
    
    results['inventory'] = addInventory(document, nodeDict, quantity, quantity_udm, db)
    
    # update the traceability
    results['track'] = db['PhysicalGood'].update_one({'_id': document['epc']}, {'$push': {'traceability': document}})
    
    return results

# %%
def OBSERVEobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity=np.nan,
                   quantity_udm=None,
                   disposition=None,
                   bizTransactionList = None,
                   bizStep=None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    
    results = {}
    document = defineObjectEvent(physicalGoodDict=physicalGoodDict,
                   nodeDict=nodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=sourceDestList,
                   ilmd=ilmd,
                   extensions=extensions)
    
    document['action'] = "OBSERVE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    results['insert'] = db['ObjectEvent'].insert_one(document)
    
    # update the traceability
    results['track'] = db['PhysicalGood'].update_one({'_id': document['epc']}, {'$push': {'traceability': document}})
    
    
    
    return results


# %%
def DELETEobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition=None,
                   bizTransactionList = None,
                   bizStep=None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    results={}
    
    document = defineObjectEvent(physicalGoodDict=physicalGoodDict,
                   nodeDict=nodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=sourceDestList,
                   ilmd=ilmd,
                   extensions=extensions)
    
    document['action'] = "DELETE"
    
    #insert record
    db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
    results['insert'] = db['ObjectEvent'].insert_one(document)
    
    #update the inventory function
    results['inventory'] = deleteInventory(document, nodeDict, quantity, quantity_udm, db)
    
    # update the traceability
    results['track'] = db['PhysicalGood'].update_one({'_id': document['epc']}, {'$push': {'traceability': document}})
    
    
    return results