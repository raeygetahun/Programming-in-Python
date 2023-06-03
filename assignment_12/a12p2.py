import turtle

def draw_face():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()

    # Draw the head
    turtle.circle(100)

    # Draw the eyes
    turtle.penup()
    turtle.goto(-40, 30)
    turtle.pendown()
    turtle.circle(20)

    turtle.penup()
    turtle.goto(40, 30)
    turtle.pendown()
    turtle.circle(20)

    # Draw the nose
    turtle.penup()
    turtle.goto(0, 10)
    turtle.pendown()
    turtle.goto(-20, -30)
    turtle.goto(20, -30)
    turtle.goto(0, 10)

    # Draw the mouth
    turtle.penup()
    turtle.goto(-40, -60)
    turtle.pendown()
    turtle.goto(40, -60)
    turtle.goto(0, -80)
    turtle.goto(-40, -60)

    # Draw the ears
    turtle.penup()
    turtle.goto(-160, 0)
    turtle.pendown()
    turtle.circle(30)

    turtle.penup()
    turtle.goto(160, 0)
    turtle.pendown()
    turtle.circle(30)

    turtle.hideturtle()
    turtle.done()

draw_face()
