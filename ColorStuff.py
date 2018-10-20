from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce

cl = ColorSensor()

RGBColor = namedtuple('r', 'g', 'b')

knownColors = {'null': RGBColor(0, 0, 0)}


def getColor():
	oldMode = cl.mode
	cl.mode='RGB-RAW'
	r = cl.value(0)
    g = cl.value(1)
    b = cl.value(2)
    c1.mode = oldMode
    return RGBColor(r, g, b)

def start():
    //turnLeft(30)

def getDistance(color1, color2):
    return sqrt(pow(color1.r-color2-r, 2) + pow(color1.g-color2.g,2) + pow(color1.b-color2.b))

def getClosestKnown(color1):
    dists = zip(knownColors, knownColors.map(lambda x: getDistance(color1, x)))
    return min(knownColors, key=lambda t: t[1])


def learnRight(colors, name):
    trimLeft = colors.copy()
    trimRight = colors.copy()
    n = len(colors)
    trimRight[1] = reduce((lambda x, y): x* (y*1.0/(n-1)))
    for ind in iter(range(1, right)):
        trimLeft[ind] = trimLeft[ind-1]*1.0*ind/(ind+1)+trimLeft[ind]*1.0/(ind+1)
        trimRight[ind] = trimRight[ind] - (n-ind)*colors[ind]
