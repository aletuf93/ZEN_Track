'''
dispensed
disposed
partially_dispensed
stolen
'''

accepting_disp=['damaged','in_progress']
arriving_disp=['in_progress']
commissioning_disp=['active']
departing_disp=['in_transit']
decommissioning=['inactive']
destroying_disp=['destroyed']
encoding_disp=['encoded']
holding_disp=['expired','no_pedigree_match','non_sellable_other','recalled',
              'returned''sellable_not_accessible']
inspecting_disp=['damaged','non_sellable_other','sellable_not_accessible']
loading_disp=['in_progress','sellable_not_accessible']
picking_disp=['in_progress']
receiving_disp=['damaged','in_progress']
removing_disp=['damaged']
receiving_disp=['returned','sellable_accessible','sellable_not_accessible']
repairing_disp=['damaged']
replacing_disp=['damaged']
reserving_disp=['reserved']
retail_selling_disp=['retail_sold']
shipping_disp=['in_transit','returned']
staging_outbound_disp=['container_closed','expired','in_progress','no_pedigree_match',
                       'non_sellable_other','recalled']
stocking_disp=['sellable_accessible']
storing_disp=['expired','no_pedigree_match','non_sellable_other','recalled',
              'sellable_not_accessible']
void_shipping_disp=['in_progress']




# %%
def accepting():
    '''
    Denotes a specific activity within a business process where an object 
    changes possession and/or ownership.
    '''
    pass

# %%
def arriving():
    '''
    Denotes a specific activity within a business process where an object 
    arrives at a location.
    '''
    pass

# %%
def assembling():
    '''
    Denotes an activity within a business process whereby one or more objects 
    are combined to create a new finished product.
    In contrast to transformation, in the output of assembling the original 
    objects are still recognisable and/or the process is reversible; hence, 
    assembling would be used in an Aggregation Event, not a Transformation Event.
    '''
    pass

# %%
def collecting():
    '''
    Denotes a specific activity within a business process where an object is 
    picked up and collected for future disposal, recycling or re-used.
    '''
    pass

# %%
def commissioning():
    '''
    Process of associating an instance-level identifier (such as an EPC) 
    with a specific object, or the process of associating a class-level 
    identifier, not previously used, with one or more objects. A tag may have 
    been encoded and applied in this step, or may have been previously encoded.
    In the case of a class-level identifier, commissioning differs from 
    creating_class_instance in that commissioning always indicates that 
    this is the first use of the class-level identifier, whereas 
    creating_class_instance does not specify whether the class-level 
    identifier has been used before.
    '''
    pass

# %%
def consigning():
    '''
    Indicates the overall process of staging_outbound, loading, departing, 
    and accepting. It may be used when more granular process step information 
    is unknown or inaccessible.
    The use of consigning is mutually exclusive from the use of 
    staging_outbound, loading, departing, and accepting.
    Note: This business step is similar to shipping, but includes a 
    change of possession and/or ownership at the outbound side.
    '''
    pass

# %%
def creating_class_instance():
    '''
    Denotes a step in a business process where an instance or increased 
    quantity of a class-level identifier is produced. Unlike commissioning, 
    this business step may be repeated for the same class-level identifier.
    '''
    pass

# %%
def cycle_counting():
    '''
    Process of counting objects within a location in order to obtain an 
    accurate inventory for business needs other than accounting purposes 
    (e.g., replenishment and allocation).
    '''
    pass

# %%
def decommissioning():
    '''
    Process of disassociating an instance-level identifier (such as an EPC) 
    with an object. The object may be re-commissioned at some point in the 
    future – however only with a new instance-level identifier.
    '''
    pass

# %%
def departing():
    '''
    Denotes a specific activity within a business process where an object 
    leaves a location on its way to a destination.
    '''
    pass

# %%
def destroying():
    '''
    Process of terminating an object. For an instance-level identifier, 
    the object should not be the subject of subsequent events; subsequent 
    events are likely indicative of error (such as a stray read of a tag 
    inside an incinerator). For a class level identifier, quantities are 
    reduced; however, the class-level identifier may still be used in 
    subsequent events (referring to different instances that were not destroyed).
    '''
    pass

# %%
def disassembling():
    '''
    Denotes a specific activity within a business process where an object 
    is broken down into separate, uniquely identified component parts.
    '''
    pass

# %%
def dispensing():
    '''
    Denotes a specific activity within a business process where a product 
    is made available in full or part to a consumer.
    '''
    pass

# %%
def encoding():
    '''
    Process of writing an instance-level identifier (typically an EPC) 
    to a barcode or RFID tag, where the identifier is not yet associated 
    with an object at this step in the process.
    '''
    pass

# %%
def entering_exiting():
    '''
    Denotes a specific activity at the Entrance/Exit door of a facility 
    where customers are either leaving with purchased product or entering 
    with product to be returned to the facility.
    '''
    pass

# %%
def holding():
    '''
    Denotes a specific activity within a business process where an object is 
    segregated for further review.
    '''
    pass

# %%
def inspecting():
    '''
    Process of reviewing objects to address potential physical or 
    documentation defects.
    '''
    pass

# %%
def installing():
    '''
    Denotes a specific activity within a business process where an object 
    is put into a composite object (not merely a container).
    In installing the composite object exists prior to this step, whereas 
    in assembling the composite object is created during the step.
    '''
    pass

# %%
def killing():
    '''
    Process of terminating an RFID tag previously associated with an object. 
    The object and its instance-level identifier may continue to exist and be 
    the subject of subsequent events (via a barcode, manual data entry, 
    replacement tag, etc.).
    '''
    pass

# %%
def loading():
    '''
    Denotes a specific activity within a business process where an object is 
    loaded into shipping conveyance.
    '''
    pass

# %%
def packing():
    '''
    Denotes a specific activity within a business process that includes 
    putting objects into a larger container – usually for shipping. 
    Aggregation of one unit to another typically occurs at this point.
    '''
    pass

# %%
def picking():
    '''
    Denotes a specific activity within a business process that includes the 
    selecting of objects to fill an order.
    '''
    pass

# %%
def receiving():
    '''
    Denotes a specific activity within a business process that indicates 
    that an object is being received at a location and is added to the receiver's inventory.
    The use of receiving is mutually exclusive from the use of arriving and accepting.
    '''
    pass

# %%
def removing():
    '''
    Denotes a specific activity within a business process where an object is 
    taken out of a composite object.
    '''
    pass

# %%
def repackaging():
    '''
    Denotes a specific activity within a business process where an 
    object’s packaging configuration is changed.
    '''
    pass

# %%
def repairing():
    '''
    Denotes a specific activity within a business process where 
    a malfunctioning product is repaired (typically by a post-sales service), 
    without replacing it by a new one.
    '''
    pass

# %%
def replacing():
    '''
    Denotes a specific activity within a business process where an object 
    is substituted or exchanged for another object.
    '''
    pass

# %%
def reserving():
    '''
    Process in which a set of instance-level identifiers, not yet 
    commissioned, are provided for use by another party.
    '''
    pass

# %%
def retail_selling():
    '''
    Denotes a specific activity within a business process at a point-of-sale 
    for the purpose of transferring ownership to a customer in exchange for 
    something of value (currency, credit, etc.).
    '''
    pass

# %%
def shipping():
    '''
    Indicates the overall process of staging_outbound, loading and departing. 
    It may be used when more granular process step information is unknown or 
    inaccessible. It may indicate a final event from a shipping point.
    The use of shipping is mutually exclusive from the use of staging_outbound, 
    departing, or loading.
    '''
    pass

# %%
def staging_outbound():
    '''
    Denotes a specific activity within a business process in which an object 
    moves from a facility to an area where it will await transport pick-up.
    '''
    pass

# %%
def stock_taking():
    '''
    Process of counting objects within a location following established 
    rules and/or standards to serve as a basis for accounting purposes.
    '''
    pass

# %%
def stocking():
    '''
    Denotes a specific activity within a business process within a location 
    to make an object available to the customer or for order fulfilment 
    within a DC.
    '''
    pass

# %%
def storing():
    '''
    Denotes a specific activity within a business process where an object is 
    moved into and out of storage within a location.
    '''
    pass

# %%
def transporting():
    '''
    Process of moving an object from one location to another using a 
    vehicle (e.g., a ship, a train, a lorry, an aircraft).
    '''
    pass

# %%
def unloading():
    '''
    Denotes a specific activity within a business process where an object 
    is unloaded from a shipping conveyance.
    '''
    pass

# %%
def unpacking():
    '''
    Denotes a specific activity within a business process that includes 
    removing products (individuals, inners, cases, pallets) from a larger 
    container – usually after receiving or accepting. Disaggregation of one 
    unit from another typically occurs at this point.
    '''
    pass

# %%
def void_shipping():
    '''
    Denotes a process of declaring that one or more objects in a prior outbound 
    process (captured in an EPCIS event having business step shipping, departing, 
    or consigning) were not shipped (or departed or consigned) as previously indicated.
    '''
    pass