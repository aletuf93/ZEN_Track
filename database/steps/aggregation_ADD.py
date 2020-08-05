from database.events.AggregationEvent import ADDaggregationEvent

# %%
def assembling(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB"):
    '''
    Denotes an activity within a business process whereby one or more objects 
    are combined to create a new finished product.
    In contrast to transformation, in the output of assembling the original 
    objects are still recognisable and/or the process is reversible; hence, 
    assembling would be used in an Aggregation Event, not a Transformation Event.
    AGGREGATION - ADD
    '''
    bizStep='assembling'
    result = ADDaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=nodeDict,
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions,
                    dbname="EPCIS_DB")
    return result

# %%
def packing(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process that includes 
    putting objects into a larger container – usually for shipping. 
    Aggregation of one unit to another typically occurs at this point.
    AGGREGATION - ADD
    '''
    bizStep='packing'
    result = ADDaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=nodeDict,
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions,
                    dbname="EPCIS_DB")
    return result

# %%
def repackaging(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an 
    object’s packaging configuration is changed.
    AGGREGATION - ADD
    '''
    bizStep='repackaging'
    result = ADDaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=nodeDict,
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions,
                    dbname="EPCIS_DB")
    return result
