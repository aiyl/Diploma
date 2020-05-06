import skimage
from skimage import io, color
mtl1= 'isba1.mtl'
mtl2= 'isbaForBlend.mtl'
def getDiffuseColor (path):
    f = open(path)
    line = f.readline()
    a = []
    while True:
        if 'Kd' in line:
            a.append(line.split(' '))
        line = f.readline()
        if not line:
            break
    for i in range (len(a)):
        a[i].remove(a[i][0])
    f.close()
    return a
def findMinDiff (list1, list2) :
    maxPoint = 100 * len(list2)
    errors = 0
    for i in range(len(list2)):
        min = 300
        for m in range(len(list1)):
            for k in range(len(list2[0])):
                list1[m][k] = float(list1[m][k])
                list2[i][k] = float(list2[i][k])
            lab1 = color.rgb2lab([[list1[m]]],'D65','2')
            lab2 = color.rgb2lab([[list2[i]]],'D65','2')
            if min > skimage.color.deltaE_cie76(lab1, lab2):
                min = skimage.color.deltaE_cie76(lab1, lab2)
                min1 = list1[m]
                min2 = list2[i]
        print('List1 ', min1)
        print('List2 ', min2)
        if min < 2.5:
            min = 0
        print(min)
        errors += round(float(min))

    points = round(((maxPoint - errors) * 100)/maxPoint)
    print('Errors', errors, 'Points ', points, 'Max Point', maxPoint)
findMinDiff(getDiffuseColor(mtl1), getDiffuseColor(mtl2))
print('участник ',getDiffuseColor(mtl1), '\n', 'эталон ',  getDiffuseColor(mtl2))