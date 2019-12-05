import bpy
import os
from mathutils import Euler, Vector

root = os.path.dirname(bpy.data.filepath)
solve_obj = bpy.ops.import_scene.obj(filepath=os.path.join(root, 'solve.obj'))

fin = os.path.join(root, 'input.txt')
fout = os.path.join(root, 'output.png')
    
with open(os.path.join(root, fin), "r") as f:
    tx, ty, tz = tuple([ float(x) for x in f.readline().split() ])
    rx, ry, rz = tuple([ float(x) for x in f.readline().split() ])
    
    cam = bpy.data.objects["Camera2"]
    cam.location = Vector((tx, ty, tz))
    cam.rotation_euler = Euler((rx, ry, rz), 'XYZ')
    
    scene = bpy.context.scene
    scene.camera = cam
    scene.render.filepath = fout
    bpy.ops.render.render(write_still=True)
