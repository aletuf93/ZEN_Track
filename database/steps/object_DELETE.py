import numpy as np
from database.events.ObjectEvent import DELETEobjectEvent


# %%
decommissioning_disp=['inactive']

def decommissioning(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition='inactive',
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Process of disassociating an instance-level identifier (such as an EPC) 
    with an object. The object may be re-commissioned at some point in the 
    future – however only with a new instance-level identifier.
    OBJECT - DELETE
    '''
    bizStep='decommissioning'
    if disposition in decommissioning_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {decommissioning_disp}")
    return result

# %%
destroying_disp=['destroyed']

def destroying(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='destroyed',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Process of terminating an object. For an instance-level identifier, 
    the object should not be the subject of subsequent events; subsequent 
    events are likely indicative of error (such as a stray read of a tag 
    inside an incinerator). For a class level identifier, quantities are 
    reduced; however, the class-level identifier may still be used in 
    subsequent events (referring to different instances that were not destroyed).
    OBJECT - DELETE
    '''
    bizStep='destroying'
    if disposition in destroying_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {destroying_disp}")
    return result

# %%
dispensing_disp=['dispensed','partially_dispensed']
def dispensing(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='dispensed',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where a product 
    is made available in full or part to a consumer.
    OBJECT - DELETE
    '''
    bizStep='dispensing'
    if disposition in dispensing_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {dispensing_disp}")
    return result

# %%
holding_disp=['expired','no_pedigree_match','non_sellable_other','recalled',
              'returned','sellable_not_accessible']

def holding(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='no_pedigree_match',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object is 
    segregated for further review.
    OBJECT - DELETE
    '''
    bizStep='holding'
    if disposition in holding_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {holding_disp}")
    return result

# %%
picking_disp=['in_progress']

def picking(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='in_progress',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process that includes the 
    selecting of objects to fill an order.
    OBJECT - DELETE
    '''
    bizStep='picking'
    if disposition in picking_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {picking_disp}")
    return result

# %%
removing_disp=['damaged','stolen']

def removing(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='damaged',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object is 
    taken out of a composite object.
    OBJECT - DELETE
    '''
    bizStep='removing'
    if disposition in removing_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {removing_disp}")
    return result

# %%
reserving_disp=['reserved']

def reserving(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='reserved',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Process in which a set of instance-level identifiers, not yet 
    commissioned, are provided for use by another party.
    OBJECT - DELETE
    '''
    bizStep='reserving'
    if disposition in reserving_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {reserving_disp}")
    return result

# %%
def unloading(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition=None,
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    is unloaded from a shipping conveyance.
    OBJECT - DELETE
    '''
    bizStep='unloading'
    
    result = DELETEobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity=quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=sourceDestList,
                   ilmd=ilmd,
                   extensions=extensions,
                   dbname="EPCIS_DB")
    
    return result

# %%
void_shipping_disp=['in_progress']
def void_shipping(physicalGoodDict,
                nodeDict,
                quantity,
                quantity_udm,
                disposition='in_progress',
                bizTransactionList = None,
                sourceDestList=[],
                ilmd=None,
                extensions={},
                dbname="EPCIS_DB"):
    '''
    Denotes a process of declaring that one or more objects in a prior outbound 
    process (captured in an EPCIS event having business step shipping, departing, 
    or consigning) were not shipped (or departed or consigned) as previously indicated.
    OBJECT - DELETE
    '''
    bizStep='void_shipping'
    if disposition in void_shipping_disp:
        result = DELETEobjectEvent(physicalGoodDict,
                       nodeDict,
                       quantity=quantity,
                       quantity_udm=quantity_udm,
                       disposition=disposition,
                       bizTransactionList = bizTransactionList,
                       bizStep=bizStep,
                       sourceDestList=sourceDestList,
                       ilmd=ilmd,
                       extensions=extensions,
                       dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {void_shipping_disp}")
    return result