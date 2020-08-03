# -*- coding: utf-8 -*-
#import packages
import random
import numpy as np
import pandas as pd

if  __name__ == "__main__":
    print("ciao")
    import sys; sys.path.insert(0, '..') #add the above level with the package

#import dependencies
from database.entities.node import node
from database.entities.node import nodeTypeDict


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

for node in nodesDict:
    node_row = pd.DataFrame([nodesDict[node].__dict__])
    D_results = D_results.append(node_row)
    
D_results = D_results.reset_index(drop=True)