import re
handle = open("solve2.obj", "r")
fileIsObj = False
while True:
    data = handle.read(512)
    c = data.find("vt")
    if c != -1:
        fileIsObj = True
        break
    if not data:
        break
handle.close()
print(fileIsObj)