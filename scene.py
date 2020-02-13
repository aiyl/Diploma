import bpy
import os
import bmesh
from mathutils import Euler, Vector

root = os.path.dirname(bpy.data.filepath)
solve_obj = bpy.ops.import_scene.obj(filepath=os.path.join(root, 'solve2.obj'))
textPath = filepath=os.path.join(root, 'text.txt')
fin = os.path.join(root, '03.in')
fout = os.path.join(root, 'output.png')
f = open(textPath, 'w')
f.write('kokc')
f.close()
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
    #nexttt
    obj = bpy.data.objects[3]
    qua = len(obj.data.vertices)
    i=0
    while i<qua:
        print(bpy.data.scenes[0].objects[3].data.vertices[i].co.x)
        i+=1
    print(qua)
    #if "solve2" in bpy.data.meshes:
     #   mesh = bpy.data.meshes["solve2"]
       # print(len(mesh.data.vertices))
#bpy.data.scenes[0].objects['solve2'].data.vertices[15].co.x

