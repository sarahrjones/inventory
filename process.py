#output: a list of tuples of the form (Fabric, yards_needed)
def compute_fabric_usage(self, quantity):
    quantity = input('Number of garments: ')
    yards_needed = garmentfabricusage_set.values('yards_used')
    fabric_used = garmentfabricusage_set.values('fabric')
    fabric_quantity = [(fabric_used, yards_needed * quantity)]
    return fabric_quantity
