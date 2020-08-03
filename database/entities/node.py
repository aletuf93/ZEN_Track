# -*- coding: utf-8 -*-
import numpy as np
import enum


# %% definition of enumerate environments (warehouse, distribution, production)
class nodeNetwork(enum.Enum):
   warehouse = 0
   distribution_network = 1
   production_plant = 2


# %% definition of nodeTypes
warehouseList = ["StorageLocation",
                 "AcceptanceArea",
                 "DeliveryArea",
                 "FakeStorageLocation",
                 "PackingArea",
                 "ConsolidationArea",
                 "QualityControlArea",
                 "DockingArea"
                 ]

distributionList = ["Truck",
                    "Train",
                    "Vessel",
                    "Aircraft",
                    "AcceptanceArea",
                    "DeliveryArea",
                    "DockingArea"
                    ]

productionList = ["Production machine",
                    "Assembly machine",
                    "Production workbench",
                    "Assembly workbench",
                    "Buffer",
                    "AcceptanceArea",
                    "DeliveryArea",
                    ]


  
nodeTypeDict = {'warehouse':warehouseList,
            'distribution_network':distributionList,
            'production_plant':productionList}

# %% define the class node
class node: 
    nodeNet = None #identifies the network type of the node from the ones in class nodeNetwork
    nodeType = None #identifies the node type of the node from the lists in nodeTypeDict 
    nodeName = None #identifies a name for the node
    geo_position = None #identifies a position for the node using tuple of coordinates (latitude, longitude)
    plant_position = None #identifies a position for the node using tuple of coordinates (latitude, longitude)
    
    def __init__(self, nodeNet, nodeType, nodeName, geo_position=(np.nan,np.nan), plant_position = (np.nan, np.nan, np.nan)):
        
        #check a consistent environment
        if nodeNet in nodeNetwork.__members__:
            self.nodeNet=nodeNet
            
            #check a consistent node type
            if nodeType in nodeTypeDict[nodeNet]:
                self.nodeType = nodeType
            else: raise Exception(f"Unknown node type, for a {nodeNet}. Choose between {nodeTypeDict[nodeNet]}")
                
            #check a consistent geo_position
            if isinstance(geo_position,tuple) & isinstance(geo_position[0],float) & isinstance(geo_position[1],float):
                self.geo_position = geo_position
            else: raise Exception(f"Invalid geo_position. Use a tuple (latitude, lonitude) of floats")
            
            #check a consistent plant_position
            if isinstance(plant_position,tuple) & isinstance(plant_position[0],float) & isinstance(plant_position[1],float) & isinstance(plant_position[2],float):
                self.geo_position = geo_position
            else: raise Exception(f"Invalid plant_position. Use a tuple (x, y,z) of floats")
            
            self.nodeName=nodeName
                
        else:
            raise Exception(f"Unknown network type, choose between {nodeTypeDict.keys()}")
            
            
# %% return node QRCODE
            
    def returnQRcode(self):
        nodeData = self.__dict__ #convert to dict the node data
        
            
            
            
   
