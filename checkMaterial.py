def getDiffuseColor (path):
    f = open(path)
    line = f.readline()
    a = []
    while True:
        if 'Kd' in line:
            #a = [a for a in line.split(' ') ]
            a.append(line.split(' '))
        line = f.readline()
        if not line:
            break
    for i in range (len(a)):
        a[i].remove(a[i][0])
    f.close()
    return a
def findMinDiff (list1, list2) :

    for i in range(len(list2)):
        min = [1.0, 1.0, 1.0]
        sumMin = 3
        for m in range(len(list1)):
            sum = 0
            for k in  range(len(list2[0])):
                sum += abs(float(list1[m][k]) - float(list2[i][k]))
            if sumMin > sum:
                min=list1[m]
                sumMin = sum

               # if min[k] > abs(float(list1[m][k]) - float(list2[i][k])):
                    #min[k] = abs(float(list1[m][k]) - float(list2[i][k]))
                #min.append(abs(float(list1[i][k]) - float(list2[i][k])))

        print(min )


diff = []
#for i in range(len(getDiffuseColor("check_mtl_blend.mtl"))):
#    diff.append(float(getDiffuseColor("check_mtl_blend.mtl")[i]) - float(getDiffuseColor('solve2.mtl')[i]))
#print(diff)
findMinDiff(getDiffuseColor('isbaForBlend.mtl'), getDiffuseColor('Check_Material.mtl'))
print('участник ',getDiffuseColor('isbaForBlend.mtl'), '\n', 'эталон ',  getDiffuseColor('Check_Material.mtl'))
#a[0.1.2]=[h=0.5, s= ,v=0.05]