import turtle

t = turtle.Turtle()
s = turtle.Turtle()

t.hideturtle()

t.pensize(3)
t.color('blue')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

t.penup()

t.goto(-130, 130)
t.pendown()
t.color('white')
t.write(" Seni seviyorum", font=("Arial", 25, "bold"))  
turtle.done()

turtle.mainloop()
