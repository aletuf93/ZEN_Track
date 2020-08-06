# -*- coding: utf-8 -*-
import datetime

'''
class defining the specific instance of a product by using an unique
product identifier, e.g. an RFID tag
'''

class physicalGood():
    
    epc = None
    created = None
    item_class = None
    class_attributes = {}
    
    def __init__(self, epc, item_class=None):
        self.epc=epc
        self.created = datetime.datetime.utcnow()
        self.item_class=item_class
        if isinstance(item_class, dict):
            self.class_attributes = item_class.__dict__
        
