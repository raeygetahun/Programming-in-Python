import turtle

def get_user_click(x, y):
    global corner1, corner2, perimeter, area

    if corner1 is None:
        corner1 = (x, y)
    else:
        corner2 = (x, y)

        length = abs(corner2[0] - corner1[0])
        width = abs(corner2[1] - corner1[1])

        perimeter = 2 * (length + width)
        area = length * width

def draw_rectangle():
    turtle.onscreenclick(get_user_click)

    turtle.penup()
    turtle.goto(corner1)
    turtle.pendown()

    for _ in range(2):
        turtle.forward(abs(corner2[0] - corner1[0]))
        turtle.right(90)
        turtle.forward(abs(corner2[1] - corner1[1]))
        turtle.right(90)

    turtle.hideturtle()
    turtle.done()

# Initialize variables
corner1, corner2 = None, None
perimeter, area = 0, 0

# Call the function to draw the rectangle
draw_rectangle()

# Print the computed perimeter and area
print("Perimeter:", perimeter)
print("Area:", area)
