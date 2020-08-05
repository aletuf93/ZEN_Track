#import packages
import pandas as pd
import numpy as np


if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package

#import dependences
from database.steps.object_ADD import encode
from database.steps.object_OBSERVE import staging_outbound
from database.steps.aggregation_ADD import assembling, packing
from database.steps.transformation_ADD import encode, commissioning

# %%
#-tomato
#-basil
#-salt
##--tomato sauce
##--boiling
##--encode lot
##--creating class instance
##--pack in 6 bottles

# %% define entities
tomato_supplier= physicalGood("tomato")
basil_supplier= physicalGood("basil")
salt_supplier= physicalGood("salt")
tomato_sauce= physicalGood("salt")
tomato_bottle= physicalGood("tomato_product")

# %% define nodes

mixing_machine = node(nodeNet='production_plant', 
                      nodeType='ProductionMachine', 
                      nodeName='Tomato mixer 100', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

boiling_machine = node(nodeNet='production_plant', 
                      nodeType='ProductionMachine', 
                      nodeName='Tomato boiler', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

bottling_machine = node(nodeNet='production_plant', 
                      nodeType='ProductionMachine', 
                      nodeName='Tomato bottler', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))
# %%
result = assembling(physicalGoodDict_parent=tomato_supplier.__dict__,
                    physicalGoodDict_child=tomato_sauce.__dict__,
                    nodeDict=mixing_machine.__dict__,
                    #quantity_parent=1000,
                    #quantity_udm_parent="kg",
                    #quantity_child=1002,
                    #quantity_udm_child="kg",
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB")

result = assembling(physicalGoodDict_parent=basil_supplier.__dict__,
                    physicalGoodDict_child=tomato_sauce.__dict__,
                    nodeDict=mixing_machine.__dict__,
                    #quantity_parent=1,
                    #quantity_udm_parent="kg",
                    #quantity_child=1002,
                    #quantity_udm_child="kg",
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB")

result = assembling(physicalGoodDict_parent=salt_supplier.__dict__,
                    physicalGoodDict_child=tomato_sauce.__dict__,
                    nodeDict=mixing_machine.__dict__,
                    #quantity_parent=1,
                    #quantity_udm_parent="kg",
                    #quantity_child=1002,
                    #quantity_udm_child="kg",
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB")

commissioning = commissioning(physicalGoodDict_input=tomato_sauce.__dict__,
                             physicalGoodDict_output=tomato_sauce.__dict__,
                             quantity=1000.0,
                             quantity_udm='kg',
                             epcClass=None,
                             xformID=None,
                             nodeDict=None,
                             disposition=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB")



result = encoding(physicalGoodDict=tomato_bottle.__dict__,
                   nodeDict=bottling_machine.__dict__,
                   quantity=1,
                   quantity_udm='pz',
                   disposition=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB")




numBottles = int(1000/0.75)
for i in range(0,numBottles):
    result = creating_class_instance(physicalGoodDict_input=tomato_bottle.__dict__,
                                 physicalGoodDict_output=tomato_bottle.__dict__,
                                 quantity=1,
                                 quantity_udm='pz',
                                 epcClass=None,
                                 xformID=None,
                                 nodeDict=None,
                                 disposition=None,
                                 bizTransactionList=None,
                                 extensions={},
                                 dbname="EPCIS_DB")



result = packing(physicalGoodDict_parent,
                    physicalGoodDict_child,
                    nodeDict=[],
                    disposition=None,
                    bizTransactionList = None,
                    sourceDestList=[],
                    extensions={},
                    dbname="EPCIS_DB")


result = staging_outbound(physicalGoodDict,
                   nodeDict,
                   disposition='ready to ship',
                   quantity=np.nan,
                   quantity_udm=None,
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB")
