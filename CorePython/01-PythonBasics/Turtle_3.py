import turtle
import random

fred = turtle.Pen()

fred.shape("turtle")
fred.width(3)
fred.speed(0)

colors = ['red','green','blue','orange']

fred.speed(0)
# for i in range(50):
#     col = random.choice(colors)
#     fred.color(col)
#     fred.circle(i*3)
#     fred.left(10)
#
# fred.goto(400, 0)
#
# for i in range(50):
#     col = random.choice(colors)
#     fred.color(col)
#     fred.circle(i*3)
#     fred.left(10)
#
def square(size):
   for i in range(50):
       col = random.choice(colors)
       fred.color(col)
       fred.circle(i*3)
       fred.left(10)

for i in range(50):
    x = random.randrange(-200,200)
    y = random.randrange(-200,200)

    fred.up()
    fred.goto(x,y)
    fred.down()

    size = random.randrange(10,200)
    col = random.choice(colors)
    fred.color(col)
    square(size)