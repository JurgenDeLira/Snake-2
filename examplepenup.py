import turtle


t = turtle.Turtle()
t.speed(1)

formas = ["arrow", "turtle", "circle", "triangle", "square", "classic"]

for forma in formas:
    t.shape(forma)

    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.circle(50)

    t.penup()
    t.forward(100)

turtle.exitonclick()
