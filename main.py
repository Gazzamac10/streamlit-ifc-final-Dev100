import streamlit as st

import Homepage
from tools import ifchelper
import json
import ifcopenshell
import ifcopenshell.util.element as Element
##################### STREAMLIT IFC-JS COMPONENT MAGIC ######################
from pathlib import Path
from typing import Optional
import streamlit.components.v1 as components


def get_objects_data_by_class(file, class_type):
    def add_pset_attributes(psets):
        for pset_name, pset_data in psets.items():
            for property_name in pset_data.keys():
                pset_attributes.add(
                    f"{pset_name}.{property_name}"
                ) if property_name != "id" else None

    objects = file.by_type(class_type)
    objects_data = []
    pset_attributes = set()

    for object in objects:
        qtos = Element.get_psets(object, qtos_only=True)
        add_pset_attributes(qtos)
        psets = Element.get_psets(object, psets_only=True)
        add_pset_attributes(psets)
        objects_data.append(
            {
                "ExpressId": object.id(),
                "GlobalId": object.GlobalId,
                "Class": object.is_a(),
                "PredefinedType": Element.get_predefined_type(object),
                "Name": object.Name,
                "Level": Element.get_container(object).Name
                if Element.get_container(object)
                else "",
                "Type": Element.get_type(object).Name
                if Element.get_type(object)
                else "",
                "QuantitySets": qtos,
                "PropertySets": psets,
            }
        )
    return objects_data, list(pset_attributes)


def hastag(productlist):
    testelements = []
    for item in productlist:
        try:
            if item.Tag:
                testelements.append(item)
        except:
            testelements = None
    return testelements

def get_quantity_single_value(x):
    quantities_dicts = {}
    for y in x.Quantities:
        if y.is_a('IfcQuantityArea'):
            quantities_dicts.update({y.Name: y.AreaValue})
        if y.is_a('IfcQuantityLength'):
            quantities_dicts.update({y.Name: y.LengthValue})
        if y.is_a('IfcQuantityVolume'):
            quantities_dicts.update({y.Name: y.VolumeValue})
        if y.is_a('IfcQuantityCount'):
            quantities_dicts.update({y.Name: y.CountValue})
        if y.is_a('IfcQuantityWeight'):
            quantities_dicts.update({y.Name: y.WeightValue})
    return quantities_dicts

def getprops(element):
    ks = element.IsDefinedBy
    ts = element.IsTypedBy
    out1 = [item for item in ks]
    ts1 = []
    for item in ts:
        if len(item) > 0:
            ts1.append(item)
    out2 = [item for item in ts1]
    return out1, out2


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

walls = ifc_file.by_type("IfcWall")

test = get_objects_data_by_class(ifc_file,"IfcWall")

print(test[0])
