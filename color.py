from turtle import *

speed(0)
bgcolor("black")
colors = ['orange', 'white']
hideturtle()

for i in range(122):
    color(colors[i % 2])
    forward(2)
    left(3)
    circle(40)
    forward(130)
    right(180)

done()
