# -*- coding: utf-8 -*-
#import packages
import random
import numpy as np
import pandas as pd

if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package

#import dependencies
from database.entities.node import node
from database.entities.physicalGood import physicalGood
from database.entities.node import nodeTypeDict
from database.models.ObjectEvent import ADDobjectEvent, OBSERVEobjectEvent, DELETEobjectEvent
from database.models.AggregationEvent import ADDaggregationEvent, OBSERVEaggregationEvent, DELETEaggregationEvent

# %% set supply chain parameters
num_wh = 5
num_plant = 15
num_transport = 100


# supply chain extension
min_latitude = 41.413896
max_latitude = 41.945192
min_longitude = 13.972079
max_longitude = 15.056329

# plant extension
min_x = 0
max_x = 100
min_y = 0
max_y = 400
min_z = 0
max_z = 0

#num EPCs
num_EPCs = int(1e4)

#num transactions
num_obj_ADD = 20
num_obj_OBSERVE = 20
num_obj_DELETE = 20

#num transactions
num_agg_ADD = 20
num_agg_OBSERVE = 20
num_agg_DELETE = 20


# %% generate entities

nodesDict = {}
entitiesCreated = 0

def generateEntity(nodeNet, nodeNameSuffix, entitiesCreated):
    #set attribute values
    
    nodeType = random.choice(nodeTypeDict[nodeNet])
    nodeName = f"{nodeNameSuffix}_{entitiesCreated}"
    geo_position = (np.random.uniform(min_latitude,max_latitude),np.random.uniform(min_longitude,max_longitude))
    plant_position = (np.random.uniform(min_x,max_x), np.random.uniform(min_y,max_y), np.random.uniform(min_z,max_z))

    entity = node(nodeNet, nodeType, nodeName, geo_position, plant_position)
    return entity


# %% generate warehouses
nodeNet = 'warehouse'
nodeNameSuffix = 'wh'
for i in range(0,num_wh):

    entitiesCreated = entitiesCreated + 1
    nodesDict[f"{nodeNameSuffix}_{entitiesCreated}"] = generateEntity(nodeNet, nodeNameSuffix, entitiesCreated)
    
# %% generate warehouses
nodeNet = 'distribution_network'
nodeNameSuffix = 'dist'
for i in range(0,num_transport):

    entitiesCreated = entitiesCreated + 1
    nodesDict[f"{nodeNameSuffix}_{entitiesCreated}"] = generateEntity(nodeNet, nodeNameSuffix, entitiesCreated)
    
# %% generate warehouses
nodeNet = 'production_plant'
nodeNameSuffix = 'prod'
for i in range(0,num_transport):

    entitiesCreated = entitiesCreated + 1
    nodesDict[f"{nodeNameSuffix}_{entitiesCreated}"] = generateEntity(nodeNet, nodeNameSuffix, entitiesCreated)   



# %% export nodes
D_results = pd.DataFrame()

for singleNode in nodesDict:
    node_row = pd.DataFrame([nodesDict[singleNode].__dict__])
    D_results = D_results.append(node_row)
    
D_results = D_results.reset_index(drop=True)


# %% generate EPCs
EPCsDict={}
for i in range(0,num_EPCs):
    EPCsDict[i] = physicalGood(f"prod_{i}")
    


# %% define objectEvents

#add objsect
for i in range (0,num_obj_ADD):

    #random choose a node
    node_key = random.choice(list(nodesDict.keys()))
    chooseNode = nodesDict[node_key]
    
    #random coose an epc
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc= EPCsDict[epc_key]
    
    
    
    result = ADDobjectEvent(physicalGood=chooseEpc,
                       nodeDict=chooseNode.__dict__,
                       )
  
#observe object
for i in range (0,num_obj_OBSERVE):

    #random choose a node
    node_key = random.choice(list(nodesDict.keys()))
    chooseNode = nodesDict[node_key]
    
    #random coose an epc
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc= EPCsDict[epc_key]
    
    
    
    result = OBSERVEobjectEvent(physicalGood=chooseEpc,
                       nodeDict=chooseNode.__dict__,
                       )
    
#delete object
for i in range (0,num_obj_OBSERVE):

    #random choose a node
    node_key = random.choice(list(nodesDict.keys()))
    chooseNode = nodesDict[node_key]
    
    #random coose an epc
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc= EPCsDict[epc_key]
    
    
    
    result = DELETEobjectEvent(physicalGood=chooseEpc,
                       nodeDict=chooseNode.__dict__,
                       )
    

# %%

#add aggregation
for i in range (0,num_agg_ADD):

        
    #random coose an epc_parent
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc_parent= EPCsDict[epc_key]
    
    #random coose an epc_parent
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc_child= EPCsDict[epc_key]
    
    
    
    result = ADDaggregationEvent(physicalGood_parent=chooseEpc_parent,
                    physicalGood_child=chooseEpc_child,
                    )
    
#observe aggregation
for i in range (0,num_agg_OBSERVE):

        
    #random coose an epc_parent
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc_parent= EPCsDict[epc_key]
    
    #random coose an epc_parent
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc_child= EPCsDict[epc_key]
    
    
    
    result = OBSERVEaggregationEvent(physicalGood_parent=chooseEpc_parent,
                    physicalGood_child=chooseEpc_child,
                    )
    
#delete aggregation
for i in range (0,num_agg_DELETE):

        
    #random coose an epc_parent
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc_parent= EPCsDict[epc_key]
    
    #random coose an epc_parent
    epc_key = random.choice(list(EPCsDict.keys()))
    chooseEpc_child= EPCsDict[epc_key]
    
    
    
    result = DELETEaggregationEvent(physicalGood_parent=chooseEpc_parent,
                    physicalGood_child=chooseEpc_child,
                    )

