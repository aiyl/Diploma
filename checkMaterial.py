import skimage
from skimage import io, color

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
    min = 300.0
    for i in range(len(list2)):
        for m in range(len(list1)):
            for k in range(len(list2[0])):
                list1[m][k] = float(list1[m][k])
                list2[i][k] = float(list2[i][k])
            #print('List1 ', list1[m])
            lab1 = color.rgb2lab([[list1[m]]],'D65','2')
            lab2 = color.rgb2lab([[list2[i]]],'D65','2')
            #print(lab1)
            #print('List2 ',list2[i])
            #print(lab2)
            #print('lol ',skimage.color.deltaE_ciede94(lab1, lab2, 2, 0.048, 0.014))
            if min > skimage.color.deltaE_cie76(lab1, lab2):
                min = skimage.color.deltaE_cie76(lab1, lab2)
                min1 = list1[m]
                min2 = list2[i]
            #print('Delta ',skimage.color.deltaE_cie76(lab1, lab2))
        print('List1 ', min1)
        print('List2 ', min2)
        print(min)
findMinDiff(getDiffuseColor('check2.mtl'), getDiffuseColor('check1.mtl'))
print('участник ',getDiffuseColor('check2.mtl'), '\n', 'эталон ',  getDiffuseColor('check1.mtl'))

#a[0.1.2]=[h=0.5, s= ,v=0.05]