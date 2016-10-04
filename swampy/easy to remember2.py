from shapes_new import *
world = TurtleWorld()
Titan = Turtle()
Titan.delay=.05

def houseFrame(t, size=10):
    square(t, size * 10)
    move(t, 0, size * 10)
    tri(t, size * 10, size * 7, size * 7)
    move(t, 0, size *-10)
    
def door(t, size = 10):
    rect(t,size * 3, size*5)

def house(t, size = 10):
    houseFrame(t, size)
    move(t, size*6, 0)
    door(t, size)
    window(t, size)
    
    
def window (t, size = 10):
    move(t, size * -5, size * 6)
    Titan.fd(size * 2)
    Titan.rt(90)
    Titan.fd(size * 4)
    Titan.lt(90)
    Titan.fd(size * 2)
    Titan.lt(90)
    Titan.fd(size * 2)
    Titan.lt(90)
    Titan.fd(size * 4)
    Titan.rt(90)
    Titan.fd(size * 2)
    Titan.rt(90)
    Titan.fd(size * 4)
    Titan.rt(90)
    Titan.fd(size * 4)
    Titan.rt(90)
    Titan.fd(size * 4)
    Titan.rt(90)
    Titan.fd(size * 4)
    move(t, size * -6, size * 1)
    Titan.rt(90)
    
    
def Chimney (t, size = 10):
    move (t, size * 5, size * 10)
    
house(Titan)

wait_for_user()
