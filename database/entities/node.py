# -*- coding: utf-8 -*-

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
    
    def __init__(self, nodeNet, nodeType):
        
        #check a consistent environment
        if nodeNet in nodeNetwork.__members__:
            self.nodeNet=nodeNet
            
            #check a consistent node type
            if nodeType in nodeTypeDict[nodeNet]:
                self.nodeType = nodeType
            else:
                raise Exception(f"Unknown node type, for a {nodeNet}. Choose between {nodeTypeDict[nodeNet]}")
                
        else:
            raise Exception(f"Unknown network type, choose between {nodeTypeDict.keys()}")
            
   
