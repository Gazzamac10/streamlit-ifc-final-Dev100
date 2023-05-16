import streamlit as st

import Homepage
from tools import ifchelper
import json
import ifcopenshell
##################### STREAMLIT IFC-JS COMPONENT MAGIC ######################
from pathlib import Path
from typing import Optional
import streamlit.components.v1 as components

st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

# Tell streamlit that there is a component called ifc_js_viewer,
# and that the code to display that component is in the "frontend" folder
frontend_dir = 'pages/frontend-viewer'
_component_func = components.declare_component(
    "ifc_js_viewer", path=str(frontend_dir)
)

# Create the python function that will be called
def ifc_js_viewer(url: Optional[str] = None):
    component_value = _component_func(url=url)
    return component_value

def draw_3d_viewer(file):
    ifc_js_viewer(file)

filepath = 'IFC/01.ifc'
file = ifcopenshell.file.from_string(filepath)

with open(filepath, 'rb') as f:
    ifc_bytes = f.read()

test = bytearray(ifc_bytes)

draw_3d_viewer(test)

#products = file.by_type('IfcProduct')

#print(filepath)


