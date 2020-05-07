from graphics import *
def getCoordXY (path):
    f = open(path)
    line = f.readline()
    a = []
    while True:
        if 'Vector' in line:
            pos = line.find('((')
            a.append(line[pos+2:len(line)-3].split(','))
        line = f.readline()
        if not line:
            break
    f.close()
    return a
def frawLine(x1, y1, x2, y2):
    win = GraphWin("Окно для графики", 500, 500)
    obj = Line(Point(x1, y1), Point(x2, y2))
    obj.setOutline("blue")
    obj.draw(win)
    win.getMouse()
    win.close()

print(getCoordXY('text.txt'))