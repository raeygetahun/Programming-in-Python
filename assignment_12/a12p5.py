from graphics import *
import random

def compute_pi(d, num_points):
    win = GraphWin("Approximating π", d, d, autoflush=False)
    win.setCoords(0, 0, d, d)
    center = Point(d/2, d/2)
    radius = d/2

    circle = Circle(center, radius)
    circle.setWidth(2)
    circle.draw(win)

    count_inside_circle = 0

    for i in range(num_points):
        x = random.uniform(0, d)
        y = random.uniform(0, d)
        point = Point(x, y)

        if ((x - d/2)**2 + (y - d/2)**2) <= (d**2)/4:
            point.setFill("red")
            count_inside_circle += 1
        else:
            point.setFill("blue")

        point.draw(win)

        if (i + 1) % 100 == 0:
            ratio = count_inside_circle / (i + 1)
            approximate_pi = ratio * 4
            print(f"Approximation after {i + 1} points: {approximate_pi}")

    win.update()
    win.getMouse()
    win.close()


d = 400
num_points = 10000

compute_pi(d, num_points)
