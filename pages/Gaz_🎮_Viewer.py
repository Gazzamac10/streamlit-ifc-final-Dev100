import streamlit as st

import Homepage
from tools import ifchelper
import json
import ifcopenshell
##################### STREAMLIT IFC-JS COMPONENT MAGIC ######################
from pathlib import Path
from typing import Optional
import streamlit.components.v1 as components

# Tell streamlit that there is a component called ifc_js_viewer,
# and that the code to display that component is in the "frontend" folder
frontend_dir = 'frontend-viewer'
_component_func = components.declare_component(
    "ifc_js_viewer", path=str(frontend_dir)
)

# Create the python function that will be called
def ifc_js_viewer(url: Optional[str] = None):
    component_value = _component_func(url=url)
    return component_value

#filename = "FLB-ACM-XX-ZZ-M3-AR-000001_S0_P01.ifc"
#ifc_file = ifcopenshell.open(filename)


def draw_3d_viewer(ifc_file_path):
    ifc_file = ifcopenshell.file(ifc_file_path)
    ifc_js_response = ifc_js_viewer(ifc_file.by_type("IfcProduct"))
    st.sidebar.success("Visualiser loaded")
    return ifc_js_response

def execute(ifc_file_path):
    draw_3d_viewer(ifc_file_path)

#execute("IFC/FLB-ACM-XX-ZZ-M3-AR-000001_S0_P01.ifc")

