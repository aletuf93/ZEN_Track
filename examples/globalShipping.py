#import packages
import pandas as pd
import numpy as np


if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package
    
#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.node import node
from database.steps.object_OBSERVE import staging_outbound, departing, accepting
from database.steps.object_ADD import loading
from database.steps.object_DELETE import unloading
from database.steps.transaction_OBSERVE import transporting
# %% set

num_containers = 120

# %% generate inbound list

bol_number="R_HK_037672"
listNumber='PICKLIST_00023481'
pickerCode='CRANE_006'
source=('terminal','outbound')
D_list = pd.DataFrame(columns=['epc','quantity'])


for i in range(0,num_containers):
    

    EPCs= physicalGood(f"container_{i}")
    temp = pd.DataFrame([EPCs],columns=['epc'])
    D_list = D_list.append(temp)
    
    
# %% define control points

loadingPort = node(nodeNet='distribution_network', 
                      nodeType='DockingArea', 
                      nodeName='Export terminal Asia', 
                      geo_position=(51.9496,4.1453), 
                      plant_position = (1000.0, 2500.0, 0.0))

dischargingPort = node(nodeNet='distribution_network', 
                      nodeType='DockingArea', 
                      nodeName='Export terminal Europe', 
                      geo_position=(22.3193,114.1694), 
                      plant_position = (1000.0, 2500.0, 0.0))

VesselNode = node(nodeNet='distribution_network', 
                      nodeType='Vessel', 
                      nodeName='ContainerCargo', 
                      )


# %%
for index, row in D_list.iterrows():
    results = staging_outbound(physicalGoodDict = row['epc'].__dict__,
                   nodeDict = loadingPort.__dict__,
                   disposition='ready to ship',
                   quantity=1,
                   quantity_udm='container',
                   bizTransactionList = listNumber,
                   sourceDestList=source,
                   ilmd=pickerCode,
                   extensions={},
                   dbname="EPCIS_DB")
    
    result = loading(physicalGoodDict = row['epc'].__dict__,
                   nodeDict = loadingPort.__dict__,
                   disposition='in_progress',
                   quantity=1,
                   quantity_udm='container',
                   bizTransactionList = listNumber,
                   sourceDestList=source,
                   ilmd=pickerCode,
                   extensions={},
                   dbname="EPCIS_DB")


    result = departing(physicalGoodDict = row['epc'].__dict__,
                       nodeDict = loadingPort.__dict__,
                       disposition='departed',
                       quantity=1,
                       quantity_udm='container',
                       bizTransactionList = listNumber,
                       sourceDestList=source,
                       ilmd=pickerCode,
                       extensions={},
                       dbname="EPCIS_DB")
    
    result = transporting(physicalGoodDict = row['epc'].__dict__,
                   nodeDict = loadingPort.__dict__,
                   bizTransactionList = bol_number,
                   DestnodeDict = dischargingPort.__dict__,
                   quantity = 1,
                   quantity_udm = 'container',
                   parentID=[],
                   transactionType='bol',
                   extensions={},
                   dbname="EPCIS_DB")
    
    result = unloading(physicalGoodDict = row['epc'].__dict__,
                       nodeDict = dischargingPort.__dict__,
                       disposition='in_progress',
                       quantity=1,
                       quantity_udm='container',
                       bizTransactionList = listNumber,
                       sourceDestList=source,
                       ilmd=pickerCode,
                       extensions={},
                       dbname="EPCIS_DB")
     
    result = accepting(physicalGoodDict = row['epc'].__dict__,
                       nodeDict = dischargingPort.__dict__,
                       disposition='in_progress',
                       quantity=1,
                       quantity_udm='container',
                       bizTransactionList = listNumber,
                       sourceDestList=source,
                       ilmd=pickerCode,
                       extensions={},
                       dbname="EPCIS_DB")
    