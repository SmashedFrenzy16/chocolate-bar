import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.title("Chocolate Bar")
s.setup(width=800, height=600)

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Chocolate Bar", align="center",font=("Arial", 24, "normal"))


t.up()

# Rectangle

t.down()
t.color("brown")
t.begin_fill()
t.fd(72)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(72)
t.lt(90)
t.fd(90)
t.end_fill()
t.up()

# Outline

t.color("black")

t.lt(90)
t.fd(24)
t.down()
t.lt(90)
t.fd(90)
t.up()
t.rt(90)
t.fd(24)
t.rt(90)
t.down()
t.fd(90)
t.up()
t.lt(90)
t.fd(24)
t.lt(90)
t.down()
t.fd(90)
t.lt(90)
t.fd(72)
t.lt(90)
t.fd(90)
t.lt(90)
t.fd(72)
t.up()
t.lt(90)
t.fd(30)
t.lt(90)
t.down()
t.fd(72)
t.up()
t.rt(90)
t.fd(30)
t.rt(90)
t.down()
t.fd(72)

t.hideturtle()


while True:
    s.update()
