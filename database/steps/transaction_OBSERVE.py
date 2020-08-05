from database.events.TransactionEvent import OBSERVEtransactionEvent
from database.transactions.transactions import transactionList


# %%

def storing(physicalGoodDict,
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
    Denotes a specific activity within a business process where an object is 
    moved into and out of storage within a location.
    TRANSACTION - OBSERVE
    '''
    bizStep='storing'
    if transactionType in transactionList:
        result = OBSERVEtransactionEvent(physicalGoodDict,
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
def transporting(physicalGoodDict,
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
    Process of moving an object from one location to another using a 
    vehicle (e.g., a ship, a train, a lorry, an aircraft).
    TRANSACTION - OBSERVE
    '''
    transporting='storing'
    if transactionType in transactionList:
        result = OBSERVEtransactionEvent(physicalGoodDict,
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