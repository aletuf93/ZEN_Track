#import packages
import pandas as pd
import numpy as np


if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package
#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.physicalGood_class import physicalGood_class
from database.entities.node import node
from database.steps.object_OBSERVE import accepting, arriving, inspecting
from database.steps.object_ADD import stocking

# %% set

num_inbound_SKUs = 25
min_qty = 1
max_qty = 100

# %% generate sku master file
tomato_sauce_6bottle_class = physicalGood_class(item_code = "000000001s2231s2",
                                        item_description = "Pack 6 bottle of tomato sauce",
                                        item_weight = 7.2,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "TomatoCompany")


# %% generate inbound list

listNumber='LIST_000001'
pickerCode='OPERATOR_02'
source=('truck','inbound')
D_list = pd.DataFrame(columns=['epc','quantity'])


for i in range(0,num_inbound_SKUs):
    

    EPCs= physicalGood(f"prod_{i}",tomato_sauce_6bottle_class)
    temp = pd.DataFrame([EPCs],columns=['epc'])
    temp['quantity'] = np.random.uniform(min_qty,max_qty)
    D_list = D_list.append(temp)
    
# %% define control points
acceptanceAreaNode = node(nodeId='wh_01',
                          nodeNet='warehouse', 
                      nodeType='AcceptanceArea', 
                      nodeName='Material receiving - inbound', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (150.0, 200.0, 0.0))


qualityControlAreaNode = node(nodeId='wh_02',
                              nodeNet='warehouse', 
                      nodeType='AcceptanceArea', 
                      nodeName='Quality control - inbound', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (150.0, 150.0, 0.0))

storageAreaNode = node(nodeId='wh_03',
                       nodeNet='warehouse', 
                      nodeType='StorageLocation', 
                      nodeName='Pallet rack', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))
    
    
# %% accept epc
for index, row in D_list.iterrows():
    results = arriving(       physicalGoodDict=row['epc'].__dict__,
                               nodeDict=acceptanceAreaNode.__dict__,
                               disposition='in_progress',
                               quantity=row['quantity'],
                               quantity_udm='Kg',
                               bizTransactionList = listNumber,
                               sourceDestList=[source],
                               ilmd=pickerCode,
                               extensions={},
                               dbname="EPCIS_DB")
    
    
    results = inspecting(       physicalGoodDict=row['epc'].__dict__,
                               nodeDict=qualityControlAreaNode.__dict__,
                               disposition='OK',
                               quantity=row['quantity'],
                               quantity_udm='Kg',
                               bizTransactionList = listNumber,
                               sourceDestList=[source],
                               ilmd=pickerCode,
                               extensions={},
                               dbname="EPCIS_DB")
    
    results = accepting(       physicalGoodDict=row['epc'].__dict__,
                               nodeDict=acceptanceAreaNode.__dict__,
                               disposition='accepted',
                               quantity=row['quantity'],
                               quantity_udm='Kg',
                               bizTransactionList = listNumber,
                               sourceDestList=[source],
                               ilmd=pickerCode,
                               extensions={},
                               dbname="EPCIS_DB")
    
    result = stocking(physicalGoodDict = row['epc'].__dict__,
                   nodeDict = storageAreaNode.__dict__,
                   quantity = row['quantity'],
                   quantity_udm='Kg',
                   disposition='sellable_accessible',
                   bizTransactionList = listNumber,
                   sourceDestList=[],
                   ilmd=pickerCode,
                   extensions={},
                   dbname="EPCIS_DB")
    


