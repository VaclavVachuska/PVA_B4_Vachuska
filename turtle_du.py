"""
#schody

from turtle import *

x = int(input("zadej pocet schodu: "))
y = int(input("zadej velikost schodu: "))
i = 0

speed(100)

while i <= x:
    left(90)
    forward(y)
    right(90)
    forward(y)
    i += 1

right(90)
forward(x*y+y)
right(90)
forward(x*y+y)

exitonclick()
"""

"""
#sestiuhelnik

from turtle import *

delka = 50
speed(100)

for i in range(1,7):
    for x in range(1,7):
        left(60)
        forward(delka)
    right(60)
    forward(delka)

exitonclick()
"""
#slunicko

from turtle import *

mezera = 30
carka = 50

speed(100)
pencolor("yellow")
pensize(10)
circle(100)
right(67.5)

for i in range(1,10):
    right(22.5)
    penup()
    forward(mezera)
    pendown()
    forward(carka)
    left(180)
    penup()
    forward(mezera+carka)
    right(22.5)
    forward(200)
    pendown()

exitonclick()
