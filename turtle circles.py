from turtle import *
bgcolor("grey")
speed(0.01)
hideturtle()
for disco in range(120):
    color("yellow")
    circle(disco)
    color("blue")
    circle(disco * 0.8)
    right(2)
    forward(2)

for spin in range(120):
    color("red")
    circle(spin)
    color("lightgreen")
    circle(spin * 0.8)
    left(2)
    backward(2)
done()
