def getDiffuseColor (path):
    f = open(path)
    line = f.readline()
    bool = True
    while bool:
        if 'Kd' in line:
            bool = False
            print(line)
        line = f.readline()
    f.close()

getDiffuseColor("solve2.mtl")
