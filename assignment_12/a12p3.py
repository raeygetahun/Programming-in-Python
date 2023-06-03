import turtle

def draw_archery(circles):
    colors = ["yellow", "red", "blue", "black", "white"]
    
    turtle.speed(0)  # Set speed
    
    for x, y, radius in circles:
        color = colors[circles.index((x, y, radius)) % len(colors)]
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
    
    turtle.done()

draw_archery([(100, 100, 15), (100, 100, 30), (100, 100, 45), (100, 100, 60), (100, 100, 75)])
