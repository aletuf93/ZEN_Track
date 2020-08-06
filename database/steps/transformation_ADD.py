from database.events.TransformationEvent import ADDtransformationEvent


# %%
commissioning_disp=['active']

def commissioning(physicalGoodDict_input,
                             physicalGoodDict_output,
                             quantity_in=1,
                             quantity_in_udm=None,
                             quantity_out=1,
                             quantity_out_udm=None,
                             epcClass=None,
                             xformID=None,
                             nodeDict=None,
                             disposition=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
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
    bizStep='commissioning'
    if disposition in commissioning_disp:
        result = ADDtransformationEvent(physicalGoodDict_input,
                             physicalGoodDict_output,
                             epcClass=epcClass,
                             xformID=xformID,
                             quantity_in=quantity_in,
                             quantity_in_udm=quantity_in_udm,
                             quantity_out=quantity_out,
                             quantity_out_udm=quantity_out_udm,
                             nodeDict=nodeDict,
                             disposition=disposition,
                             bizStep=bizStep,
                             bizTransactionList=bizTransactionList,
                             extensions={},
                             dbname="EPCIS_DB")
    else:
        raise Exception(f"Invalid disposition '{disposition}' for step '{bizStep}', chose between {commissioning_disp}")
    return result

# %%
def creating_class_instance(physicalGoodDict_input,
                             physicalGoodDict_output,
                             quantity_in=1,
                             quantity_in_udm=None,
                             quantity_out=1,
                             quantity_out_udm=None,
                             epcClass=None,
                             xformID=None,
                             nodeDict=None,
                             disposition=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB"):
    '''
    Denotes a step in a business process where an instance or increased 
    quantity of a class-level identifier is produced. Unlike commissioning, 
    this business step may be repeated for the same class-level identifier.
    TRANSFORMATION - ADD
    '''
    bizStep='creating_class_instance'
    
    result = ADDtransformationEvent(physicalGoodDict_input,
                         physicalGoodDict_output,
                         epcClass=epcClass,
                         xformID=xformID,
                         quantity_in=quantity_in,
                         quantity_in_udm=quantity_in_udm,
                         quantity_out=quantity_out,
                         quantity_out_udm=quantity_out_udm,
                         nodeDict=nodeDict,
                         disposition=disposition,
                         bizStep=bizStep,
                         bizTransactionList=bizTransactionList,
                         extensions={},
                         dbname="EPCIS_DB")
    return result