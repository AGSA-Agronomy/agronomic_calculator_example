def acres_to_hectare(acres):
    """This function converts area in acres to hectares"""
    return acres * 0.404686

def gwv_to_vwc(gwc, bd):
    """ Convert Gravimetric Water Content into 
    Volumetric Content using bulk density of soil"""
    return gwc * bd

def wheat_bu_to_wheat_ton(wbu, wton):
    """ Convert Wheat (bu) to Wheat (Ton)"""
    return wbu * 0.027216
