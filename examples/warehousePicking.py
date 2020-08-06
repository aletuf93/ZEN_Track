#import packages
import pandas as pd
import numpy as np
import random


if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package
#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.physicalGood_class import physicalGood_class
from database.entities.node import node
from database.steps.object_OBSERVE import staging_outbound, departing
from database.steps.object_ADD import loading
from database.steps.object_DELETE import picking
from database.steps.aggregation_ADD import packing



# %% set

num_outbound_SKUs = 25
min_qty = 1
max_qty = 10

# %% generate sku master file
tomato_sauce_bottle_class = physicalGood_class(item_code = "000000001s2231",
                                        item_description = "bottle of tomato sauce",
                                        item_weight = 1.2,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "TomatoCompany")

tomato_sauce_6bottle_class = physicalGood_class(item_code = "000000001s2231s2",
                                        item_description = "Pack 6 bottle of tomato sauce",
                                        item_weight = 7.2,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "TomatoCompany")

tomato = physicalGood_class(            item_code = "0001",
                                        item_description = "tomato",
                                        item_weight = None,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "supplier")

basil = physicalGood_class(             item_code = "0002",
                                        item_description = "basil",
                                        item_weight = None,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "supplier")

salt = physicalGood_class(              item_code = "0002",
                                        item_description = "salt",
                                        item_weight = None,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "supplier")

sku_master_file = {'tomato_sauce_bottle_class':tomato_sauce_bottle_class,
                   'tomato_sauce_6bottle_class':tomato_sauce_6bottle_class,
                   'tomato':tomato,
                   'basil':basil,
                   'salt':salt,
             
    }

# %% define control points

storageAreaNode = node(nodeId='wh_03',
                       nodeNet='warehouse', 
                      nodeType='StorageLocation', 
                      nodeName='Pallet rack', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

outboundAreaNode = node(nodeId='wh_04',
                        nodeNet='warehouse', 
                      nodeType='DeliveryArea', 
                      nodeName='Shipping area', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

TruckNode = node(nodeId='tr_road_01_FO0892341',
                 nodeNet='distribution_network', 
                      nodeType='Truck', 
                      nodeName='MarioTruck_01', 
                      )

# %% generate outbound list

listNumber='PICKLIST_00023481'
pickerCode='PICKER_006'
source=('warehouse','outbound')
D_list = pd.DataFrame(columns=['epc','quantity'])


for i in range(0,num_outbound_SKUs):
    
    sku = random.choice(list(sku_master_file.keys()))
    EPCs= physicalGood(f"prod_{i}",sku_master_file[sku])
    
    temp = pd.DataFrame([EPCs],columns=['epc'])
    temp['quantity'] = np.random.uniform(min_qty,max_qty)
    D_list = D_list.append(temp)
    

    
    
# %% accept epc
for index, row in D_list.iterrows():
    results = picking(physicalGoodDict = row['epc'].__dict__,
                nodeDict = storageAreaNode.__dict__,
                quantity = row['quantity'],
                quantity_udm='Kg',
                disposition='in_progress',
                bizTransactionList = listNumber,
                sourceDestList=[],
                ilmd=pickerCode,
                extensions={},
                dbname="EPCIS_DB")
    

    
# %% define a single pallet load

EPCs_pallet= physicalGood("PALLET_0001")  

# %% aggregate on the pallet
for index, row in D_list.iterrows():
    results = packing(physicalGoodDict_parent = row['epc'].__dict__,
                    physicalGoodDict_child = EPCs_pallet.__dict__,
                    nodeDict=outboundAreaNode.__dict__,
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB")
    
# %% ship the pallet
result = staging_outbound(physicalGoodDict = EPCs_pallet.__dict__,
                   nodeDict = outboundAreaNode.__dict__,
                   disposition='ready to ship',
                   quantity=1,
                   quantity_udm='pallet',
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB")

result = loading(physicalGoodDict = EPCs_pallet.__dict__,
                   nodeDict = TruckNode.__dict__,
                   disposition='in_progress',
                   quantity=1,
                   quantity_udm='pallet',
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB")

result = departing(physicalGoodDict = EPCs_pallet.__dict__,
                   nodeDict = TruckNode.__dict__,
                   disposition='departed',
                   quantity=1,
                   quantity_udm='pallet',
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB")
    
    


