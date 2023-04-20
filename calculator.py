def acres_to_hectare(acres):
    """This function converts area in acres to hectares"""
    return acres * 0.404686

def gwv_to_vwc(gwc, bd):
    """ Convert Gravimetric Water Content into 
    Volumetric Content using bulk density of soil"""
    return gwc * bd
