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


def callback_upload():
    session["array_buffer"] = session["uploaded_file"].getvalue()
    session["ifc_file"] = ifcopenshell.file.from_string(session["array_buffer"].decode("utf-8"))


st.sidebar.header('Model Loader')
st.sidebar.file_uploader("Choose a file", type=['ifc'], key="uploaded_file", on_change=callback_upload)

session = st.session_state


def get_current_ifc_file():
    return session.array_buffer

def draw_3d_viewer():
    ifc_js_viewer(get_current_ifc_file())

def execute():
    draw_3d_viewer()

execute()

st.write(get_current_ifc_file())

