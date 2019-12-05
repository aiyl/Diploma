import bpy
import os
import random as rnd
import time
from mathutils import Euler, Vector

root = os.path.dirname(bpy.data.filepath)
testDir = os.path.join(root, "tests")
os.makedirs(testDir, exist_ok=True)

solve_obj = bpy.ops.import_scene.obj(filepath=os.path.join(root, 'solve.obj'))
cam = bpy.data.objects["Camera"]

def cam_init():
    cam.location = Vector((0, 0, 0))
    cam.rotation_euler = Euler((0, 0, 0), 'XYZ')

def create_test(frame_idx, testnum):
    bpy.context.scene.frame_set(frame_idx)
    
    t = cam.matrix_world.to_translation()
    r = cam.matrix_world.to_euler("XYZ")

    with open(os.path.join(testDir, "{:02}.in".format(testnum)), "w") as fin:
        fin.write("{:.6f} {:.6f} {:.6f}\n".format(t.x, t.y, t.z))
        fin.write("{:.6f} {:.6f} {:.6f}".format(r.x, r.y, r.z))

    scene = bpy.context.scene
    scene.render.filepath = os.path.join(testDir, str(frame_idx))
    bpy.ops.render.render(write_still=True)

    os.rename(os.path.join(testDir, str(frame_idx) + ".png"), os.path.join(testDir, "{:02d}.png".format(testnum)))


rnd.seed(10)

frames = list(range(100))
for i in range(len(frames)):
    j = rnd.randint(i, len(frames) - 1)
    frames[i], frames[j] = frames[j], frames[i]

# cam_init()
for i in range(1, 21):
    create_test(frames[i], i)