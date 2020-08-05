#import packages



if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package
#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.node import node

from database.steps.object_DELETE import removing
from database.steps.object_OBSERVE import replacing
from database.steps.object_ADD import installing
# %% define control points
maintenanceReport="REP_000001"
operatorId="MAIN_OPER_005"
milling_machine = node(nodeNet='production_plant', 
                      nodeType='ProductionMachine', 
                      nodeName='Pallet rack', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

old_part= physicalGood("electronic_board_01")  
new_part= physicalGood("electronic_board_02") 

# %%

result = removing(physicalGoodDict=old_part.__dict__,
                nodeDict = milling_machine.__dict__,
                quantity = 1,
                quantity_udm = 'pz',
                disposition='damaged',
                bizTransactionList = maintenanceReport,
                sourceDestList=[],
                ilmd=operatorId,
                extensions={},
                dbname="EPCIS_DB")

result = replacing(physicalGoodDict = old_part.__dict__,
                   nodeDict = milling_machine.__dict__,
                   disposition='replaced',
                   quantity=1,
                   quantity_udm= ' pz',
                   bizTransactionList = maintenanceReport,
                   sourceDestList=[],
                   ilmd=operatorId,
                   extensions={},
                   dbname="EPCIS_DB")


result = installing(physicalGoodDict = new_part.__dict__,
                   nodeDict = milling_machine.__dict__,
                   quantity = 1,
                   quantity_udm = 'pz',
                   disposition=None,
                   bizTransactionList = maintenanceReport,
                   sourceDestList=[],
                   ilmd=operatorId,
                   extensions={},
                   dbname="EPCIS_DB")