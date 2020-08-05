#import packages
import pandas as pd
import numpy as np


if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package
#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.node import node
from database.steps.object_OBSERVE import accepting, arriving

# %% set

num_inbound_SKUs = 25
min_qty = 1
max_qty = 100
# %% generate inbound list

listNumber='LIST_000001'
pickerCode='OPERATOR_02'
source=('truck','inbound')
D_list = pd.DataFrame(columns=['epc','quantity'])


for i in range(0,num_inbound_SKUs):
    

    EPCs= physicalGood(f"prod_{i}")
    temp = pd.DataFrame([EPCs],columns=['epc'])
    temp['quantity'] = np.random.uniform(min_qty,max_qty)
    D_list = D_list.append(temp)
    
# %% define control points
acceptanceAreaNode = node(nodeNet='warehouse', 
                      nodeType='AcceptanceArea', 
                      nodeName='Material receiving - inbound', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (150.0, 200.0, 0.0))
    
    
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
    


