from graphics import *
import random
import sys

def compute_pi(d, num_points):
    if not (0 < d <= 1000 and num_points > 0):
        print("Invalid parameters.")
        sys.exit(1)

    win = GraphWin("Approximating π", d, d)
    win.setCoords(0, 0, d, d)
    circle = Circle(Point(d/2, d/2), d/2)
    circle.setWidth(2)
    circle.draw(win)

    count_inside_circle = 0

    for i in range(num_points):
        x, y = random.uniform(0, d), random.uniform(0, d)
        point = Point(x, y)
        point.setFill("red" if (x - d/2)**2 + (y - d/2)**2 <= (d**2)/4 else "blue")
        point.draw(win)

        if (i + 1) % 100 == 0:
            ratio = count_inside_circle / (i + 1)
            approximate_pi = ratio * 4
            print(f"Approximation after {i + 1} points: {approximate_pi}")

    win.getMouse()
    win.close()

if len(sys.argv) != 3:
    print("Invalid number of parameters.")
    sys.exit(1)

try:
    window_size, num_points = map(int, sys.argv[1:])
except ValueError:
    print("Invalid parameters.")
    sys.exit(1)

compute_pi(window_size, num_points)
