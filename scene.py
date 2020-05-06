import bpy
import os
import bmesh
from mathutils import Euler, Vector

root = os.path.dirname(bpy.data.filepath)
solve_obj = bpy.ops.import_scene.obj(filepath=os.path.join(root, 'check1.obj'))
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
    bpy.context.scene.render.film_transparent = True
    scene.render.filepath = fout
    bpy.ops.render.render(write_still=True)
    #nexttt
    #
    obj = bpy.data.objects[1]
    mesh = bpy.data.meshes[0]
    quaVer = len(obj.data.vertices)
    quaFaces = len(obj.data.polygons)
    quaEdges = len(obj.data.edges)
    n = len(bpy.data.objects) - 3
    print('количество объектов на сцене', n)
    i = 0
    k = 0
    check = 0
   #все вершины и их координаты
   # while i<quaVer:
        #print(bpy.data.scenes[0].objects[3].data.vertices[i].co.x)
        #i+=1

    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='VERT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_non_manifold()
        bpy.ops.object.editmode_toggle()
        #print([vertex.select for vertex in bpy.context.selected_objects[0].data.vertices])

        while i<quaVer:
            if obj.data.vertices[i].select == True:
                #print('Non manifold loops:  ', obj.data.vertices[i].co)
                k+=1

            #print(obj.data.vertices[i].select)
            i += 1
       # print("in edit mode and selected none manifold ")
        print('non manifold vertex quantity: ', k)
    else:
        print('poll failed')
    #bpy.ops.mesh.select_non_manifold()
    #bpy.ops.mesh.print3d_clean_non_manifold()
    while i < quaFaces:
        if len(obj.data.polygons[i].vertices) == 3 or 4:
            check += 1
        i += 1
    if check == quaFaces:
        print("geometry is OK")
    else:
        print('wrong geometry')


    #определенное колво моделей на сцене, проверка нормали,                    начличие материалла, свойства матер ??? mtl файл, uv развертку (у каждого полигона текстура) развертка не менее 80%, сделай прозрачный рендер, полигоны не перескаются в uv развертке
    print('vertices ', quaVer)
    print('faces ', quaFaces)
    print('edges ', quaEdges)
    print(bpy.context.object.active_material)
    # bpy.data.objects[3].active_material только материаллы выбранных объектов

    # UV
    me = bpy.context.object.data
    uv_layer = me.uv_layers.active.data

    for poly in me.polygons:
        print("Polygon index: %d, length: %d" % (poly.index, poly.loop_total))

        # range is used here to show how the polygons reference loops,
        # for convenience 'poly.loop_indices' can be used instead.
        for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
            print("    Vertex: %d" % me.loops[loop_index].vertex_index)
            print("    UV: %r" % uv_layer[loop_index].uv)


# bpy.context.edit_object - на данный момент выбранный в edit mode object
   #bpy.context.active_object - активный
    #bpy.context.scene.tool_settings.uv_select_mode = 'FACE'
    #bpy.ops.sculpt.uv_sculpt_stroke() ?????



# v- вектора, vt - текстура vn - нормали vp -  параметры вершин в пространстве
# bpy.ops.uv.export_layout(filepath="", export_all=False, modified=False, mode='PNG', size=(1024, 1024), opacity=0.25) export UV to file
