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
    quaVer = len(obj.data.vertices)
    quaFaces = len(obj.data.polygons)
    quaEdges = len(obj.data.edges)
    i = 0
    check = 0
   #все вершины и их координаты
   # while i<quaVer:
        #print(bpy.data.scenes[0].objects[3].data.vertices[i].co.x)
        #i+=1
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='EDIT')
        print("in edit mode ")
    else:
        print('poll failed')
    #bpy.ops.mesh.print3d_clean_non_manifold()
    while i < quaFaces:
        if len(obj.data.polygons[i].vertices) == 3 or 4:
            check += 1
        i += 1
    if check == quaFaces:
        print("geometry is OK")
    else:
        print('wrong geometry')
    print('vertexes ', quaVer)
    print('faces ', quaFaces)
    print('edges ', quaEdges)

