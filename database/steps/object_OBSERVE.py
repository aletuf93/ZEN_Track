import numpy as np
from database.events.ObjectEvent import OBSERVEobjectEvent

# %%
accepting_disp=['damaged','in_progress','accepted']
def accepting(     physicalGoodDict,
                   nodeDict,
                   disposition='accepted',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    changes possession and/or ownership.
    OBJECT - OBSERVE
    '''
    bizStep='accepting'
    if disposition in accepting_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {accepting_disp}")
    return result

# %%
arriving_disp=['in_progress','received']

def arriving(physicalGoodDict,
                   nodeDict,
                   disposition='received',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    arrives at a location.
    OBJECT - OBSERVE
    '''
    bizStep='arriving'
    if disposition in arriving_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {arriving_disp}")
    return result
# %%
def cycle_counting(physicalGoodDict,
                   nodeDict,
                   disposition=None,
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Process of counting objects within a location in order to obtain an 
    accurate inventory for business needs other than accounting purposes 
    (e.g., replenishment and allocation).
    OBJECT - OBSERVE
    '''
    bizStep='cycle_counting'
    result = OBSERVEobjectEvent(physicalGoodDict,
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
departing_disp=['departed','in_transit']

def departing(physicalGoodDict,
                   nodeDict,
                   disposition='departed',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    leaves a location on its way to a destination.
    OBJECT - OBSERVE
    '''
    bizStep='departing'
    if disposition in departing_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {departing_disp}")
    return result

# %%
entering_exiting=['entering','exiting','unknonwn']
def entering_exiting(physicalGoodDict,
                   nodeDict,
                   disposition='unknonwn',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity at the Entrance/Exit door of a facility 
    where customers are either leaving with purchased product or entering 
    with product to be returned to the facility.
    OBJECT - OBSERVE
    '''
    bizStep='entering_exiting'
    if disposition in entering_exiting:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {entering_exiting}")
    return result

# %%
inspecting_disp=['OK','damaged','non_sellable_other','sellable_not_accessible','stolen']

def inspecting(physicalGoodDict,
                   nodeDict,
                   disposition='OK',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Process of reviewing objects to address potential physical or 
    documentation defects.
    OBJECT - OBSERVE
    '''
    bizStep='inspecting'
    if disposition in inspecting_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {inspecting_disp}")
    return result
# %%
repairing_disp=['damaged','repaired']

def repairing(physicalGoodDict,
                   nodeDict,
                   disposition='repaired',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where 
    a malfunctioning product is repaired (typically by a post-sales service), 
    without replacing it by a new one.
    OBJECT - OBSERVE
    '''
    bizStep='repairing'
    if disposition in repairing_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {repairing_disp}")
    return result    
# %%
replacing_disp=['replaced','damaged']

def replacing(physicalGoodDict,
                   nodeDict,
                   disposition='replaced',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    is substituted or exchanged for another object.
    OBJECT - OBSERVE
    '''
    bizStep='replacing'
    if disposition in replacing_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {replacing_disp}")
    return result    
# %%
staging_outbound_disp=['ready to ship','container_closed','expired','in_progress','no_pedigree_match',
                       'non_sellable_other','recalled']

def staging_outbound(physicalGoodDict,
                   nodeDict,
                   disposition='ready to ship',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process in which an object 
    moves from a facility to an area where it will await transport pick-up.
    OBJECT-OBSERVE
    '''
    bizStep='staging_outbound'
    if disposition in staging_outbound_disp:
        result = OBSERVEobjectEvent(physicalGoodDict,
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
        raise Exception(f"Invalid disposition 'f{disposition}' for step '{bizStep}', chose between {staging_outbound_disp}")
    return result    
# %%
def stock_taking(physicalGoodDict,
                   nodeDict,
                   disposition=None,
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Process of counting objects within a location following established 
    rules and/or standards to serve as a basis for accounting purposes.
    OBJECT - OBSERVE
    '''
    bizStep='stock_taking'
    result = OBSERVEobjectEvent(physicalGoodDict,
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
    