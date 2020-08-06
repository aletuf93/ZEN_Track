# -*- coding: utf-8 -*-
import datetime

import database.mongo_loginManager as mdb
from database.entities.physicalGood_class import physicalGood_class
'''
class defining the specific instance of a product by using an unique
product identifier, e.g. an RFID tag
'''

class physicalGood():
    
    epc = None
    created = None
    item_class = None
    class_attributes = {}
    
    def __init__(self, epc, item_class=None, dbname='EPCIS_DB'):
        self.epc=epc
        self.created = datetime.datetime.utcnow()
        #self.item_class=item_class
        if isinstance(item_class, physicalGood_class):
            self.class_attributes = item_class.__dict__
            
        #save the record into the database
        db, dbname = mdb.setConnectionPymongo(dbname, not_enc=True)
        
        #check if the record already exists
        find = db['PhysicalGood'].find_one({'_id': epc})
        
            
        if find == None: # if not found
            document = {}
            
            for key in list(self.__dict__.keys()):
                
                #unpack if a dictionary
                if isinstance(self.__dict__[key],dict):
                        for key_child in list(self.__dict__[key].keys()):
                            document[key_child] = self.__dict__[key][key_child]
                        
                elif key == 'epc': #set epc as _id
                    document['_id'] = self.__dict__['epc']
                else:
                    document[key] = self.__dict__[key]
                
                
                
            print(document)
                
                    
            document['traceability'] = []
            print(document)
            
            result = db['PhysicalGood'].insert_one(document)
        
