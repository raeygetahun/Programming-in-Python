from graphics import *

win = GraphWin("Color Pixels", 255, 255)

for i in range(255*255):
    color = color_rgb(i % 256, i % 256, i % 256)
    point = Point(i % 255, i // 255)
    point.setFill(color)
    point.plotPixelFast(win)
    if i % 150 == 0:
        point.plotPixel(win)

win.getMouse()
win.close()
