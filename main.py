import numpy as np
import scipy.misc as smp
import random
from random import randrange
from PIL import Image, ImageDraw

class Point:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

def getmiddle(A,B):
    return (A+B)/2

iterations = 500000

im = Image.new('RGB', (1000, 1000), (255,255,255))
draw = ImageDraw.Draw(im)

triSize = 100

A = Point(500, 0)
B = Point(950, 250)
C = Point(50, 250)
D = Point(800, 800)
E = Point(200, 800)

#Draw first points
draw.point((A.x,A.y), fill=(0,0,0))
draw.point((B.x,B.y), fill=(0,0,0))
draw.point((C.x,C.y), fill=(0,0,0))
draw.point((D.x,D.y), fill=(0,0,0))

#pick first random point
ranPoint = Point(randrange(50, 250), (randrange(10, 150)))
sav = randrange(5)
for temp in range(iterations):
    ran = randrange(5)
    while ran == sav:
        ran = randrange(5)
    sav = ran

    if ran == 0:
        newX = getmiddle(A.x, ranPoint.x)
        newY = getmiddle(A.y, ranPoint.y)
        draw.point((newX, newY), fill=(255, 155, 0))
        ranPoint = Point(newX, newY)

    if ran == 1:
        newX = getmiddle(B.x, ranPoint.x)
        newY = getmiddle(B.y, ranPoint.y)
        draw.point((newX, newY), fill=(0, 255, 155))
        ranPoint = Point(newX, newY)

    if ran == 2:
        newX = getmiddle(C.x, ranPoint.x)
        newY = getmiddle(C.y, ranPoint.y)
        draw.point((newX, newY), fill=(155, 0, 255))
        ranPoint = Point(newX, newY)

    if ran == 3:
        newX = getmiddle(D.x, ranPoint.x)
        newY = getmiddle(D.y, ranPoint.y)
        draw.point((newX, newY), fill=(255, 0, 255))
        ranPoint = Point(newX, newY)

    if ran == 4:
        newX = getmiddle(E.x, ranPoint.x)
        newY = getmiddle(E.y, ranPoint.y)
        draw.point((newX, newY), fill=(255, 0, 0))
        ranPoint = Point(newX, newY)




im.show()