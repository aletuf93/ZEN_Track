
#import dependences
from database.events.AggregationEvent import ADDaggregationEvent, OBSERVEaggregationEvent, DELETEaggregationEvent
from database.events.TransactionEvent import ADDtransactionEvent, OBSERVEtransactionEvent, DELETEtransactionEvent
from database.events.TransformationEvent import ADDtransformationEvent, OBSERVEtransformationEvent, DELETEtransformationEvent


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












