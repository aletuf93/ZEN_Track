
'''
class defining the class of a physical good (not the single specifi product)
'''

class physicalGood_class():
    
    item_code = None
    item_description = None
    item_weight = None
    item_length = None
    item_height = None
    item_width = None
    item_volume = None
    item_manufacturer = None
    
    
    
    def __init__(self, item_code = None,
                        item_description = None,
                        item_weight = None,
                        item_length = None,
                        item_height = None,
                        item_width = None,
                        item_volume = None,
                        item_manufacturer = None):
        
        self.item_code = item_code
        self.item_description = item_description
        self.item_weight = item_weight
        self.item_length = item_length
        self.item_height = item_height
        self.item_width = item_width
        self.item_volume = item_volume
        self.item_manufacturer = item_manufacturer