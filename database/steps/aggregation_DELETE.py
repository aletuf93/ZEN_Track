from database.events.TransactionEvent import DELETEaggregationEvent


# %%
def disassembling(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process where an object 
    is broken down into separate, uniquely identified component parts.
    AGGREGATION - DELETE
    '''
    bizStep='disassembling'
    result = DELETEaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions,
                    dbname="EPCIS_DB")
    return result

# %%
def unpacking(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process that includes 
    removing products (individuals, inners, cases, pallets) from a larger 
    container – usually after receiving or accepting. Disaggregation of one 
    unit from another typically occurs at this point.
    AGGREGATION - DELETE
    '''
    bizStep='unpacking'
    result = DELETEaggregationEvent(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=disposition,
                    bizTransactionList = bizTransactionList,
                    bizStep=bizStep,
                    sourceDestList=sourceDestList,
                    extensions=extensions,
                    dbname="EPCIS_DB")
    return result
