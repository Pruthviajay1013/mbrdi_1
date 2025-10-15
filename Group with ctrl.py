import maya.cmds as cmds

def create_groups_and_nurbs():
    # Get the selected objects in the scene
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    for obj in selected_objects:
        # Get the world-space position of the selected object
        position = cmds.xform(obj, query=True, worldSpace=True, translation=True)

        # Remove 'jnt' from the object name and add '_Grp' suffix to create the group name
        group_name = obj.replace("jnt", "") + "Grp"  # Remove 'jnt' and add '_Grp'

        # Create an empty group at the selected object's position
        group = cmds.group(empty=True, name=group_name)  # Create an empty group

        # Move the empty group to the selected object's position
        cmds.xform(group, worldSpace=True, translation=position)

        # Create a NURBS circle at the position of the group
        circle_name = group_name.replace("_Grp", "_Ctrl")  # Replace '_Grp' with '_Ctrl' for the NURBS circle name
        circle = cmds.circle(radius=1, normal=(0, 1, 0), name=circle_name)[0]  # Create the NURBS circle

        # Move the NURBS circle to the same position as the group
        cmds.xform(circle, worldSpace=True, translation=position)

        # Parent the NURBS circle under the group
        cmds.parent(circle, group)

    cmds.confirmDialog(title="Success", message="Groups and NURBS Circles created at selected positions!", button="OK")

# Call the function to create groups and NURBS circles at selected positions
create_groups_and_nurbs()
