from graphics import *
win = GraphWin("Окно для графики", 500, 500)
def frawLine(x1, y1, x2, y2):
    obj = Line(Point(x1, y1), Point(x2, y2))
    obj.setOutline("blue")
    obj.draw(win)
    win.getMouse()
    win.close()