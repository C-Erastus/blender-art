import bpy 
import random

space = 2.2
for x in range(10):
    for y in range(10):
        location = (x * space, y * space, random.random() *2)

        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=location)
        
        item = bpy.context.object
        if random.random() < 0.3:
            item.data.materials.append(bpy.data.materials["Material.001"])
        else:
            item.data.materials.append(bpy.data.materials["Material"])
