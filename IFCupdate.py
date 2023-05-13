import ifcopenshell
from ifcopenshell.api import run
import numpy


ifc_file = ifcopenshell.file()
project = run("root.create_entity", ifc_file, ifc_class="IfcProject", name="Demo")

run("unit.assign_unit", ifc_file, length={"is_metric": True, "raw": "METERS"})
context = run("context.add_context", ifc_file, context_type="Model")
body = run("context.add_context", ifc_file,context_type="Model", context_identifier="Body", target_view="MODEL_VIEW", parent=context)

# Create a site, building, and storey. Many hierarchies are possible.
site = run("root.create_entity", ifc_file, ifc_class="IfcSite", name="My Site")
building = run("root.create_entity", ifc_file, ifc_class="IfcBuilding", name="Building A")
storey = run("root.create_entity", ifc_file, ifc_class="IfcBuildingStorey", name="Ground Floor")

# Since the site is our top level location, assign it to the project
# Then place our building on the site, and our storey in the building
run("aggregate.assign_object", ifc_file, relating_object=project, product=site)
run("aggregate.assign_object", ifc_file, relating_object=site, product=building)
run("aggregate.assign_object", ifc_file, relating_object=building, product=storey)


def read_from_csv():
    print ('read from csv')

def create_wall():

    ifc_material = run("material.add_material", ifc_file, name="brick")
    ifc_walltype = run("root.create_entity", ifc_file, ifc_class="IfcWallType", name="wall_demo")
    relating_material = run("material.assign_material", ifc_file, product=ifc_walltype, type="IfcMaterialLayerSet")
    layer_set = relating_material.RelatingMaterial
    layer = run("material.add_layer", ifc_file, layer_set=layer_set, material=ifc_material)
    layer.LayerThickness = 0.2

    print ('hier', ifc_walltype)


    ifc_walltype_instance = run("root.create_entity", ifc_file, ifc_class="IfcWall", relating_type=ifc_walltype, name='wall_demo')

    representation = run("geometry.add_wall_representation",ifc_file,context=body,length=5,height=3,thickness=layer.LayerThickness)

    matrix_1 = numpy.array(
            (
                (1.0, 0.0, 0.0, 0.0),
                (0.0, 1.0, 0.0, 0.0),
                (0.0, 0.0, 1.0, 0.0),
                (0.0, 0.0, 0.0, 1.0),
            )
        )

    #moult snippet
    #style = ifcopenshell.api.run("style.add_style", ifc_file, name="My style")
    #run("style.add_surface_style", ifc_file, style=style, ifc_class="IfcSurfaceStyleShading", attributes={"SurfaceColour": { "Name": 'red', "Red": 1., "Green": 0., "Blue": 0. }})
    #run("style.assign_representation_styles", ifc_file, shape_representation=representation, styles=[style])

    #brunopostle gorgious snippet
    #style = run("style.add_style", ifc_file, name=ifc_material.Name)
    #run("style.add_surface_style",ifc_file,style=style,attributes={"SurfaceColour": {"Name": ifc_material.Name,"Red": 0.8,"Green": 0.5,"Blue": 0.2,},"Transparency": 0,"ReflectanceMethod": "PLASTIC",})
    #run("style.assign_material_style",ifc_file,material=ifc_material,style=style,context=context)



    run("type.assign_type", ifc_file, related_object=ifc_walltype_instance, relating_type=ifc_walltype)
    run("geometry.edit_object_placement",ifc_file,product=ifc_walltype_instance ,matrix=matrix_1)
    run("spatial.assign_container", ifc_file, relating_structure=storey, product=ifc_walltype_instance)
    run("geometry.assign_representation", ifc_file, product=ifc_walltype, representation=representation)

create_wall()