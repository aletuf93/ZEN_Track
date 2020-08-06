import numpy as np
if  __name__ == "__main__":
    import sys; sys.path.insert(0, '..') #add the above level with the package

#import dependences
from database.entities.physicalGood import physicalGood
from database.entities.physicalGood_class import physicalGood_class
from database.entities.node import node

from database.steps.object_ADD import encoding
from database.steps.object_OBSERVE import staging_outbound
from database.steps.aggregation_ADD import packing
from database.steps.transformation_ADD import creating_class_instance, commissioning

# %% production cycle
#-tomato
#-basil
#-salt
##--tomato sauce
##--boiling
##--encode lot
##--creating class instance
##--pack in 6 bottles

# %% define product master file
tomato_sauce_bottle_class = physicalGood_class(item_code = "000000001s2231",
                                        item_description = "bottle of tomato sauce",
                                        item_weight = 1.2,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "TomatoCompany")

tomato_sauce_6bottle_class = physicalGood_class(item_code = "000000001s2231s2",
                                        item_description = "Pack 6 bottle of tomato sauce",
                                        item_weight = 7.2,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "TomatoCompany")

tomato = physicalGood_class(            item_code = "0001",
                                        item_description = "tomato",
                                        item_weight = None,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "supplier")

basil = physicalGood_class(             item_code = "0002",
                                        item_description = "basil",
                                        item_weight = None,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "supplier")

salt = physicalGood_class(              item_code = "0002",
                                        item_description = "salt",
                                        item_weight = None,
                                        item_length = None,
                                        item_height = None,
                                        item_width = None,
                                        item_volume = None,
                                        item_manufacturer = "supplier")

# %% define entities
tomato_supplier= physicalGood("tomato", tomato)
basil_supplier= physicalGood("basil",basil)
salt_supplier= physicalGood("salt", salt)
tomato_sauce= physicalGood("tomato_sauce")
tomato_bottle= physicalGood("tomato_product", tomato_sauce_bottle_class)
tomato_pack_6_bottles= physicalGood("tomato_pack_6_bottles",tomato_sauce_6bottle_class)
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

outboundAreaNode = node(nodeNet='warehouse', 
                      nodeType='DeliveryArea', 
                      nodeName='Shipping area', 
                      geo_position=(41.413896,15.056329), 
                      plant_position = (1000.0, 2500.0, 0.0))

# %% define new production lot
result = encoding(physicalGoodDict=tomato_bottle.__dict__,
                   nodeDict=bottling_machine.__dict__,
                   quantity=1,
                   quantity_udm='pz',
                   disposition='encoded',
                   bizTransactionList = None,
                   sourceDestList=[],
                   ilmd=None,
                   extensions={},
                   dbname="EPCIS_DB")

# %% open new production lot
commissioning = commissioning(physicalGoodDict_input=tomato_sauce.__dict__,
                             physicalGoodDict_output=tomato_sauce.__dict__,
                             epcClass=None,
                             xformID=None,
                             nodeDict=None,
                             disposition='active',
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB")




# %% produce
result = creating_class_instance(physicalGoodDict_input = tomato_supplier.__dict__,
                             physicalGoodDict_output = tomato_sauce.__dict__,
                             quantity_in=1000,
                             quantity_in_udm='kg',
                             quantity_out=1002,
                             quantity_out_udm='kg',
                             epcClass=None,
                             xformID=None,
                             nodeDict=mixing_machine.__dict__,
                             disposition=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB")

result = creating_class_instance(physicalGoodDict_input = basil_supplier.__dict__,
                             physicalGoodDict_output = tomato_sauce.__dict__,
                             quantity_in=1,
                             quantity_in_udm='kg',
                             quantity_out=1002,
                             quantity_out_udm='kg',
                             epcClass=None,
                             xformID=None,
                             nodeDict=mixing_machine.__dict__,
                             disposition=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB")

result = creating_class_instance(physicalGoodDict_input = salt_supplier.__dict__,
                             physicalGoodDict_output = tomato_sauce.__dict__,
                             quantity_in=1,
                             quantity_in_udm='kg',
                             quantity_out=1002,
                             quantity_out_udm='kg',
                             epcClass=None,
                             xformID=None,
                             nodeDict=mixing_machine.__dict__,
                             disposition=None,
                             bizTransactionList=None,
                             extensions={},
                             dbname="EPCIS_DB")
# %% create bottles

numBottles = int(1000/0.75)
for i in range(0,numBottles):
    result = creating_class_instance(physicalGoodDict_input=tomato_sauce.__dict__,
                                 physicalGoodDict_output=tomato_bottle.__dict__,
                                 quantity_in=0.75,
                                 quantity_in_udm='kg',
                                 quantity_out=1,
                                 quantity_out_udm='pz',
                                 epcClass=None,
                                 xformID=None,
                                 nodeDict=bottling_machine.__dict__,
                                 disposition=None,
                                 bizTransactionList=None,
                                 extensions={},
                                 dbname="EPCIS_DB")

# %% create 6-bottle packages
numPackages = numBottles = int(numBottles/6)
for j in range(0,numPackages):
    for i in range(0,6):
        result = packing(physicalGoodDict_parent = tomato_bottle.__dict__,
                            physicalGoodDict_child = tomato_pack_6_bottles.__dict__,
                            nodeDict=bottling_machine.__dict__,
                            disposition=None,
                            bizTransactionList = None,
                            sourceDestList=[],
                            extensions={},
                            dbname="EPCIS_DB")


    result = staging_outbound(physicalGoodDict=tomato_pack_6_bottles.__dict__,
                       nodeDict=outboundAreaNode.__dict__,
                       disposition='ready to ship',
                       quantity=np.nan,
                       quantity_udm=None,
                       bizTransactionList = None,
                       sourceDestList=[],
                       ilmd=None,
                       extensions={},
                       dbname="EPCIS_DB")
