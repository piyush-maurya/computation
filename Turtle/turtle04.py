import turtle
import math
def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
    turtle.mainloop()
def circle(t,r):
    c = 2*r*math.pi
    polygon(t,c/25,25)
bob =  turtle.Turtle()
circle(bob,50)
