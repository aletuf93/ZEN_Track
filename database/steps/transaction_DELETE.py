from database.events.TransactionEvent import DELETEtransactionEvent
from database.transactions.transactions import transactionList

# %%
def killing(physicalGoodDict,
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
    Process of terminating an RFID tag previously associated with an object. 
    The object and its instance-level identifier may continue to exist and be 
    the subject of subsequent events (via a barcode, manual data entry, 
    replacement tag, etc.).
    TRANSACTION - DELETE
    '''
    bizStep='killing'
    if transactionType in transactionList:
        result = DELETEtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=bizStep,
                   parentID=parentID,
                   disposition=transactionType,
                   extensions=extensions,
                   dbname="EPCIS_DB")
     else:
        raise Exception(f"Invalid transaction Type '{disposition}' for step '{bizStep}', chose between {transactionList}")
    return result

# %%

def retail_selling(physicalGoodDict,
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
    Denotes a specific activity within a business process at a point-of-sale 
    for the purpose of transferring ownership to a customer in exchange for 
    something of value (currency, credit, etc.).
    TRANSACTION - DELETE
    '''
    bizStep='retail_selling'
    if transactionType in transactionList:
        result = DELETEtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=bizStep,
                   parentID=parentID,
                   disposition=transactionType,
                   extensions=extensions,
                   dbname="EPCIS_DB")
     else:
        raise Exception(f"Invalid transaction Type '{disposition}' for step '{bizStep}', chose between {transactionList}")
    return result

# %%
shipping_disp=['in_transit','returned']

def shipping(physicalGoodDict,
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
    Indicates the overall process of staging_outbound, loading and departing. 
    It may be used when more granular process step information is unknown or 
    inaccessible. It may indicate a final event from a shipping point.
    The use of shipping is mutually exclusive from the use of staging_outbound, 
    departing, or loading.
    
    TRANSACTION-DELETE
    '''
    bizStep='shipping'
    if transactionType in transactionList:
        result = DELETEtransactionEvent(physicalGoodDict,
                   nodeDict,
                   bizTransactionList,
                   DestnodeDict,
                   quantity,
                   quantity_udm,
                   bizStep=bizStep,
                   parentID=parentID,
                   disposition=transactionType,
                   extensions=extensions,
                   dbname="EPCIS_DB")
     else:
        raise Exception(f"Invalid transaction Type '{disposition}' for step '{bizStep}', chose between {transactionList}")
    return result