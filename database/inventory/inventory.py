

def addInventory(document, nodeDict, quantity, quantity_udm, db):
    #update inventory record
    if 'item_class_item_code' in document.keys():
        query_inventory = {'nodeId' : nodeDict['nodeId'],
                           'item_class_item_code' : document['item_class_item_code']}
        
        # check if it exist
        find = db['Inventory'].find_one(query_inventory)
        #print(find)
        if find == None: # if not found
            query_inventory['quantity'] = quantity
            query_inventory['quantity_udm'] = quantity_udm
            
            #add all the node information
            for key in list(nodeDict.keys()):
                if key not in query_inventory.keys():
                    query_inventory[key] = nodeDict[key]
            
            result = db['Inventory'].insert_one(query_inventory)
        else:
            result = db['Inventory'].update_one({'_id':find['_id']},
                                            {'$inc': { 'quantity': quantity }} ,
                                            upsert=True)
    return result

# %%

def deleteInventory(document, nodeDict, quantity, quantity_udm, db):
    #update inventory record
    if 'item_class_item_code' in document.keys():
        query_inventory = {'nodeId' : nodeDict['nodeId'],
                           'item_class_item_code' : document['item_class_item_code']}
        
        # check if it exist
        find = db['Inventory'].find_one(query_inventory)
        #print(find)
        if find == None: # if not found
            query_inventory['quantity'] = quantity
            query_inventory['quantity_udm'] = quantity_udm
            
            #add all the node information
            for key in list(nodeDict.keys()):
                if key not in query_inventory.keys():
                    query_inventory[key] = nodeDict[key]
            
            result = db['Inventory'].insert_one(query_inventory)
        else:
            result = db['Inventory'].update_one({'_id':find['_id']},
                                            {'$inc': { 'quantity': quantity }} ,
                                            upsert=True)
    return result
