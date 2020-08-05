from database.events.TransactionEvent import ADDtransactionEvent
from database.transactions.transactions import transactionList

# %%
def consigning(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   parentID=[],
                   transactionType='bol',
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Indicates the overall process of staging_outbound, loading, departing, 
    and accepting. It may be used when more granular process step information 
    is unknown or inaccessible.
    The use of consigning is mutually exclusive from the use of 
    staging_outbound, loading, departing, and accepting.
    Note: This business step is similar to shipping, but includes a 
    change of possession and/or ownership at the outbound side.
    TRANSACTION - ADD
    
    '''
    bizStep='consigning'
    if disposition in transactionList:
        result = ADDtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=bizStep,
                   parentID=[],
                   disposition=transactionType,
                   extensions={},
                   dbname="EPCIS_DB")
     else:
        raise Exception(f"Invalid transaction Type '{disposition}' for step '{bizStep}', chose between {transactionList}")
    return result

# %%

def receiving(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   parentID=[],
                   transactionType='bol',
                   extensions={},
                   dbname="EPCIS_DB"):
    '''
    Denotes a specific activity within a business process that indicates 
    that an object is being received at a location and is added to the receiver's inventory.
    The use of receiving is mutually exclusive from the use of arriving and accepting.
    TRANSACTION-ADD
    
    '''
    bizStep='receiving'
    if disposition in transactionList:
        result = ADDtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=bizStep,
                   parentID=[],
                   disposition=transactionType,
                   extensions={},
                   dbname="EPCIS_DB")
     else:
        raise Exception(f"Invalid transaction Type '{disposition}' for step '{bizStep}', chose between {transactionList}")
    return result

