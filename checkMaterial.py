def getDiffuseColor (path):
    f = open(path)
    line = f.readline()
    bool = True
    while bool:
        if 'Kd' in line:
            bool = False
            a = [a for a in line.split(' ') ]
        line = f.readline()
    a.remove(a[0])
    f.close()
    return a
diff = []
for i in range(len(getDiffuseColor("check_mtl_blend.mtl"))):
    diff.append(float(getDiffuseColor("check_mtl_blend.mtl")[i]) - float(getDiffuseColor('solve2.mtl')[i]))
print(diff)
print(getDiffuseColor("check_mtl_blend.mtl"), getDiffuseColor('solve2.mtl'))

