import streamlit as st

import Homepage
from tools import ifchelper
import json
import ifcopenshell
##################### STREAMLIT IFC-JS COMPONENT MAGIC ######################
from pathlib import Path
from typing import Optional
import streamlit.components.v1 as components

def hastag(productlist):
    testelements = []
    for item in productlist:
        try:
            if item.Tag:
                testelements.append(item)
        except:
            testelements = None
    return testelements


filepath = 'IFC/hello_wall.ifc'
ifc_file = ifcopenshell.open(filepath)

products = ifc_file.by_type('IfcProduct')
pnames = []
obj_info = []
for product in products:
    pnames.append(product.is_a())

uniquepPnames = (sorted([item for item in set(pnames)]))

listoflistofproducts = [ifc_file.by_type(item) for item in uniquepPnames]

elementswithtags = [hastag(item) for item in listoflistofproducts]
elementsout = [x for x in elementswithtags if x]

"""
ind = 0
testbeams = elementsout[ind]
testonebeam = testbeams[0]
testonebeam2 = testbeams[-1]
"""
print (listoflistofproducts[4][0].get_info()['id'])

print (ifc_file.by_type("IfcElement"))