#import packages
import numpy as np

#import dependences
from database.events.AggregationEvent import ADDaggregationEvent, OBSERVEaggregationEvent, DELETEaggregationEvent
from database.events.TransactionEvent import ADDtransactionEvent, OBSERVEtransactionEvent, DELETEtransactionEvent
from database.events.TransformationEvent import ADDtransformationEvent, OBSERVEtransformationEvent, DELETEtransformationEvent




# %%
def assembling():
    '''
    Denotes an activity within a business process whereby one or more objects 
    are combined to create a new finished product.
    In contrast to transformation, in the output of assembling the original 
    objects are still recognisable and/or the process is reversible; hence, 
    assembling would be used in an Aggregation Event, not a Transformation Event.
    AGGREGATION - ADD
    '''
    pass

# %%
def collecting():
    '''
    Denotes a specific activity within a business process where an object is 
    picked up and collected for future disposal, recycling or re-used.
    OBJECT - ADD
    '''
    pass

# %%
commissioning_disp=['active']

def commissioning():
    '''
    Process of associating an instance-level identifier (such as an EPC) 
    with a specific object, or the process of associating a class-level 
    identifier, not previously used, with one or more objects. A tag may have 
    been encoded and applied in this step, or may have been previously encoded.
    In the case of a class-level identifier, commissioning differs from 
    creating_class_instance in that commissioning always indicates that 
    this is the first use of the class-level identifier, whereas 
    creating_class_instance does not specify whether the class-level 
    identifier has been used before.
    TRANSFORMATION - ADD
    '''
    pass



# %%
def creating_class_instance():
    '''
    Denotes a step in a business process where an instance or increased 
    quantity of a class-level identifier is produced. Unlike commissioning, 
    this business step may be repeated for the same class-level identifier.
    TRANSFORMATION - ADD
    '''
    pass









# %%
def disassembling():
    '''
    Denotes a specific activity within a business process where an object 
    is broken down into separate, uniquely identified component parts.
    AGGREGATION - DELETE
    '''
    pass


# %%
def killing():
    '''
    Process of terminating an RFID tag previously associated with an object. 
    The object and its instance-level identifier may continue to exist and be 
    the subject of subsequent events (via a barcode, manual data entry, 
    replacement tag, etc.).
    TRANSACTION - DELETE
    '''
    pass



# %%
def packing():
    '''
    Denotes a specific activity within a business process that includes 
    putting objects into a larger container – usually for shipping. 
    Aggregation of one unit to another typically occurs at this point.
    AGGREGATION - ADD
    '''
    pass

# %%
def repackaging():
    '''
    Denotes a specific activity within a business process where an 
    object’s packaging configuration is changed.
    AGGREGATION - ADD
    '''
    pass







# %%
retail_selling_disp=['retail_sold']

def retail_selling():
    '''
    Denotes a specific activity within a business process at a point-of-sale 
    for the purpose of transferring ownership to a customer in exchange for 
    something of value (currency, credit, etc.).
    TRANSACTION - DELETE
    '''
    pass

# %%
shipping_disp=['in_transit','returned']

def shipping():
    '''
    Indicates the overall process of staging_outbound, loading and departing. 
    It may be used when more granular process step information is unknown or 
    inaccessible. It may indicate a final event from a shipping point.
    The use of shipping is mutually exclusive from the use of staging_outbound, 
    departing, or loading.
    
    TRANSACTION-DELETE
    '''
    pass

# %%
def unpacking():
    '''
    Denotes a specific activity within a business process that includes 
    removing products (individuals, inners, cases, pallets) from a larger 
    container – usually after receiving or accepting. Disaggregation of one 
    unit from another typically occurs at this point.
    AGGREGATION - DELETE
    '''
    pass

