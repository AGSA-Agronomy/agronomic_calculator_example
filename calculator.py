
def acres_to_hectare(acres):
    """This function converts area in acres to hectares"""
    return acres * 0.404686

def bu_ac_to_kg_ha(lb_ha):
    """This function converts corn grain yield in bushel per acre to kg per hectare"""
    return lb_ac / 0.0159
def lb_to_kg(lb):
    """FUnction to convert lb to kg"""
    return lb * 0.453592

def gwv_to_vwc(gwc, bd):
    """ Convert Gravimetric Water Content into 
    Volumetric Content using bulk density of soil"""
    return gwc * bd
def corn_bushel_acre_to_kg_hectare(bushels):
    """ This function converts bushels of corn per acre to kg per hectar"""
    kg_hectar = bushels *62.77
    return kg_hectar

def density(mass, volume):
    return mass / volume

