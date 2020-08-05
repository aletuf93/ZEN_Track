#import packages
import pandas as pd
import numpy as np


if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package
#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.node import node
from database.steps.object_OBSERVE import staging_outbound, departing
from database.steps.object_ADD import loading
from database.steps.object_DELETE import picking

# %% set

num_outbound_SKUs = 25
min_qty = 1
max_qty = 10
# %% generate inbound list

listNumber='PICKLIST_00023481'
pickerCode='PICKER_006'
source=('warehouse','outbound')
D_list = pd.DataFrame(columns=['epc','quantity'])


for i in range(0,num_outbound_SKUs):
    

    EPCs= physicalGood(f"prod_{i}")
    temp = pd.DataFrame([EPCs],columns=['epc'])
    temp['quantity'] = np.random.uniform(min_qty,max_qty)
    D_list = D_list.append(temp)
    
# %% define control points

storageAreaNode = node(nodeNet='warehouse', 
                      nodeType='StorageLocation', 
                      nodeName='Pallet rack', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

outboundAreaNode = node(nodeNet='warehouse', 
                      nodeType='DeliveryArea', 
                      nodeName='Shipping area', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

outboundAreaNode = node(nodeNet='distribution_network', 
                      nodeType='Truck', 
                      nodeName='MarioTruck_01', 
                      )
    
    
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
    
    
    
    


