import turtle
import random

fred = turtle.Pen()

fred.shape("turtle")
fred.width(3)
fred.speed(0)

colors = ['red','green','blue','orange']

fred.speed(0)

for i in range(150):
    col = random.choice(colors)
    fred.color(col)
    fred.forward(i+6)
    fred.left(135)
    fred.forward(i+3)
    fred.left(90)
    fred.forward(i+4)

# for i in range(5):
#     col = random.choice(colors)
#     fred.color(col)
#     fred.forward(200)
#     fred.left(135)
#     fred.forward(150)
#     fred.left(90)
#     fred.forward(160)