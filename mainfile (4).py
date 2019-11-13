#Mathew De La Cruz
import turtle

from functionfile import*

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(100)
bob.pensize(7)
turtle.bgcolor("black")

#Variables
size=55
sides=12
c=(0,0,0)

for n in range(70):
    c=(150,n,50)
    polygon(bob,sides,size,c)
    bob.right(135)
    size+=1

turtle.done()

