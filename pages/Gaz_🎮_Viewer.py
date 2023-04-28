import streamlit as st
from tools import ifchelper
import json
import ifcopenshell
##################### STREAMLIT IFC-JS COMPONENT MAGIC ######################
from pathlib import Path  #
from re import L  #
from typing import Optional  #
import streamlit.components.v1 as components  #

#                                                                           #
#                                                                           #
# Tell streamlit that there is a component called ifc_js_viewer,            #
# and that the code to display that component is in the "frontend" folder   #
frontend_dir = (Path(__file__).parent / "frontend-viewer").absolute()  #
_component_func = components.declare_component(  #
    "ifc_js_viewer", path=str(frontend_dir)  #
)  #


#                                                                           #
# Create the python function that will be called                            #
def ifc_js_viewer(  #
        url: Optional[str] = None,  #
):  #
    component_value = _component_func(  #
        url=url,  #
    )  #
    return component_value  #


#                                                                           #
#############################################################################

def draw_3d_viewer():
    def get_current_ifc_file():
        return session.array_buffer

    session.ifc_js_response = ifc_js_viewer(get_current_ifc_file())
    st.sidebar.success("Visualiser loaded")


def execute():
    st.header("🎮 IFC.js Viewer")
    if "ifc_file" in session and session["ifc_file"]:
        if "ifc_js_response" not in session:
            session["ifc_js_response"] = ""
        draw_3d_viewer()
    else:
        st.header("Step 1: Load a file from the Home Page")


session = st.session_state
execute()
