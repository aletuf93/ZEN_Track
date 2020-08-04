# -*- coding: utf-8 -*-
import mongoengine as odm


# %% DEFINE THE EVENT CLASS
class event(odm.DynamicDocument):
        
    #when
    eventTime = odm.DateTimeField(required=True) #The date and time at which the event occurred
    recordTime = odm.DateTimeField() #The date and time at which event was recorded by an EPCIS repository
    
    #what
    eventID = odm.ObjectIdField(primary_key=True, required=True) #A globally unique identifier across all the events
        #physical entity
    epcList = odm.ListField() #A list of observed EPCs naming the physical objects
    epcClass = odm.StringField() #The identifier specifying the object class to which it belongs
    parentID = odm.StringField() #The identifier of the parent of the association (container)
    childEPCs = odm.ListField() #An unordered list of the EPCs of contained objects (contained)
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
    
    #allow inheritance
    meta = { 'abstract': True,'allow_inheritance': True }
# %%