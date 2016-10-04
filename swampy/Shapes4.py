from TurtleWorld import *
from math import *


def equilateral_tri(turtle, size=100, rotate=0):
    print "Equilateral Triangle, with Size:", size, "and Rotation:", rotate
    turtle.lt(rotate)
    counter = 0
    
    while counter < 3:
        turtle.fd(size)
        turtle.lt(120)
        counter += 1
    turtle.rt(rotate)     
#--------------------------QUADRILATERALS-------------------------#

def para(turtle, width=100, height=100, big_angle=120, rotate=0):
    print "Parallelogram, with Width:", width, "Height:", height, "Large Angle:", big_angle, "and Rotation:", rotate
    counter = 0
    while counter < 2:
        turtle.fd(height)
        turtle.lt(big_angle)
        turtle.fd(width)
        turtle.lt(180-big_angle)
        counter+=1
        turtle.rt(rotate)

def rhom(turtle, size=100, big_angle=120, rotate=0):
    print "Rhombus, with Size:", size, "Large Angle:", big_angle, "and Rotation:", rotate
    counter = 0
    while counter < 2:
        turtle.fd(size)
        turtle.lt(big_angle)
        turtle.fd(size)
        turtle.lt(180-big_angle)
        counter+=1
    turtle.rt(rotate)
def rect(turtle, width=100, height=10, rotate=0):
    print "Rectangle, with Width:", width, "Height:", height, "and Rotation:", rotate
    turtle.lt(rotate)
    counter = 0
    while counter < 2:
        turtle.fd(width)
        turtle.lt(90)
        turtle.fd(height)
        turtle.lt(90)
        counter+=1
    turtle.rt(rotate)
    
def square(turtle, size=100, rotate=0):
    print "Square, with Size:", size, "and Rotation:", rotate
    turtle.lt(rotate)
    counter = 0
    while counter < 4:
        turtle.fd(size)
        turtle.lt(90)
        counter+=1
    turtle.rt(rotate)
   
    
#-------------------------------POLYGONS--------------------------#

def poly(turtle, sides=5, size=100, rotate=0):
    print "Polygon, with Sides:", sides, "Size:", size, "and Rotation:", rotate
    counter = 0 
    while counter < sides
       tirtle.fd(size)
       turtle.lt(360.0/size)
       counter += 1
def star(turtle, points=5, size=100.0, rotate=0):
    print "Star, with Points:", points, "Size:", size, "and Rotation:", rotate
    turtle.rt(rotate)
    counter = 0
    while counter < 5:
      turtle.rt(points)
      turtle.fd(size)
      turtle.rt(rotate)
      turtle.fd(size)
      counter+=1
    

#------------------------------MOVEMENT---------------------------#

def line(turtle, x=100, y=100):
    print "Line to a point X:", x, "over and Y:", y, "up"
    
  
def move(turtle, x, y):
    print "Move without marking a line to a point X:", x, "over and Y:", y, "up"

World = TurtleWorld()
Titan = Turtle()
Titan.delay = .1
#square(Titan)
#square(Titan, 100)
#square(Titan, 90, 90)
#square(Titan, 160, 160)
#square(Titan, 180,180)
#rect(Titan, 100, 60,)
#rect(Titan, 90, 50)
#rect(Titan, 160, 40)
#rect(Titan, 180, 90)
poly(Titan, 70, 40, 60)



wait_for_user()
