from database.events.ObjectEvent import ADDobjectEvent



# %%
encoding_disp=['encoded']

def encoding(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition='encoded',
                   bizTransactionList = None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Process of writing an instance-level identifier (typically an EPC) 
    to a barcode or RFID tag, where the identifier is not yet associated 
    with an object at this step in the process.
    OBJECT - ADD
    '''
    bizStep='encoding'
    if disposition in encoding_disp:
        result = ADDobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=None,
                   ilmd=ilmd,
                   extensions={},
                   dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {encoding_disp}")
    return result

# %%
def installing(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition=None,
                   bizTransactionList = None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    is put into a composite object (not merely a container).
    In installing the composite object exists prior to this step, whereas 
    in assembling the composite object is created during the step.
    OBJECT - ADD
    '''
    bizStep='installing'
    
    result = ADDobjectEvent(physicalGoodDict,
               nodeDict,
               quantity,
               quantity_udm=quantity_udm,
               disposition=disposition,
               bizTransactionList = bizTransactionList,
               bizStep=bizStep,
               sourceDestList=None,
               ilmd=ilmd,
               extensions={},
               dbname="EPCIS_DB")
   
    return result

# %%
stocking_disp=['sellable_accessible']

def stocking(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition='sellable_accessible',
                   bizTransactionList = None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process within a location 
    to make an object available to the customer or for order fulfilment 
    within a DC.
    OBJECT - ADD
    '''
    bizStep='stocking'
    if disposition in stocking_disp:
        result = ADDobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=None,
                   ilmd=ilmd,
                   extensions={},
                   dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {stocking_disp}")
    return result


# %%
loading_disp=['in_progress','sellable_not_accessible']

def loading(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm,
                   disposition='in_progress',
                   bizTransactionList = None,
                   sourceDestList=None,
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object is 
    loaded into shipping conveyance.
    OBJECT - ADD
    '''
    bizStep='loading'
    if disposition in loading_disp:
        result = ADDobjectEvent(physicalGoodDict,
                   nodeDict,
                   quantity,
                   quantity_udm=quantity_udm,
                   disposition=disposition,
                   bizTransactionList = bizTransactionList,
                   bizStep=bizStep,
                   sourceDestList=None,
                   ilmd=ilmd,
                   extensions={},
                   dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {loading_disp}")
    return result
