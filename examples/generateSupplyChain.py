# -*- coding: utf-8 -*-
#import packages
import random
import numpy as np


#import dependencies
from database.entities.node import node


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


for i in range(0,num_wh):
    
    entitiesCreated = entitiesCreated + 1 
    
    #set attribute values
    nodeNet = "warehouse"
    nodeType = random.choice(node.warehouseList)
    nodeName = f"wh_{entitiesCreated}"
    geo_position = (np.random.uniform(min_latitude,max_latitude),np.random.uniform(min_longitude,max_longitude))
    plant_position = (np.random.uniform(min_x,max_x), np.random.uniform(min_y,max_y), np.random.uniform(min_z,max_z))
    
    entity = node(nodeNet, nodeType, nodeName, geo_position, plant_position)
    
    nodesDict[nodeName] = entity
