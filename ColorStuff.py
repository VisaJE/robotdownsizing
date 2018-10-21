from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce
from math import *

class ColorStuff:
    def __init__(self):
        self.cl = ColorSensor()
        RGBColor = namedtuple('RGBColor', 'r g b')
        self.RGBColor = namedtuple('RGBColor', 'r g b')
        self.knownColors = {'null': RGBColor(10, 10, 10), 'changeRed': RGBColor(125, 138, 193), 'ground': RGBColor(32, 50, 35), 'tape': RGBColor(134, 163, 175), 'dimRed': RGBColor(147, 38, 193)}
        self.differenceThreshold = 28

    # Returns tuple (seen color name, is the color within the threshold)
    def getColorFUCK(self):
        res = self.getColor(self.getColorH())
        print(res)
        return res

# Returns tuple (seen color name, is the color within the threshold)
    def getAvrColorFUCK(self):
        col = self.getAvrColor()
        res = self.getColor(col)
        print(res)
        return (res, self.getDistance(self.knownColors(res), col)) 

    def getColorH(self):
        oldMode = self.cl.mode
        self.cl.mode='RGB-RAW'
        r = self.cl.value(0)
        g = self.cl.value(1)
        b = self.cl.value(2)
        self.cl.mode = oldMode
        #print("mitattu " + str(r) + " " + str(g) + " " + str(b))
        return self.RGBColor(r, g, b)

    def getDistance(self, color1, color2):
        return sqrt(pow(color1.r-color2.r, 2) + pow(color1.g-color2.g,2) + pow(color1.b-color2.b, 2))

    def getClosestKnown(self, color1):
        dists = zip(self.knownColors.items(), map((lambda x: self.getDistance(color1, x[1]) ), self.knownColors.items() ))
        dists = list(dists)
        #print("mita vi" + str(len(dists)))
        #for i in dists:
        #    print(i)
        return min(dists, key=lambda t: t[1])

    def getColor(self, color):
        found = self.getClosestKnown(color)
        return (found[0][0], found[1] < self.differenceThreshold)

    def learnColor(self, name):
        col = self.getAvrColor()
        if self.getColor(col)[1]:
            return False
        else self.knownColors[name] = col

    def learnColorRight(self, colors, name):
        trimLeft = colors.copy()
        trimRight = colors.copy()
        n = len(colors)
        trimRight[1] = reduce((lambda x, y: (x[0]* (y[0]*1.0/(n-1), x[1]* (y[1]*1.0/(n-1), x[2]* (y[2]*1.0/(n-1)))))))
        for ind in range(1, n-1):
            for i in ('r', 'g', 'b'):
                trimLeft[ind][i] = trimLeft[ind-1][i]*1.0*ind/(ind+1)+trimLeft[ind][i]*1.0/(ind+1)
                trimRight[ind+1][i] = (trimRight[ind][i]*(n-ind) - colors[ind][i])/(n-ind-1)
        trimLeft = map(lambda a: self.getDistance(trimLeft[a], trimRight[a]), range(n))
        trimLeft[0] = 0
        trimLeft[n-1] = 0
        found = max(zip(trimLeft, range(n)), key= lambda a: a[0])
        print("Found biggest difference in avr color at index {}\n".format(found))
        if trimLeft[found] > self.differenceThreshold:
            knownColors[name] = trimRight[found]
            return True
        else:
            return False

    def getAvrColor(self):
        color = self.getColorH()
        for i in range(9):
            sleep(0.1)
            newCol = self.getColorH()
            color.r = color.r + newCol. r
            color.g = color.g + newCol.g
            color.b = color.b + newCol.b
        color.r = color.r /10
        color.g = color.g /10
        color.b = color.b /10

    def findColorFromRight(self, name):
        colors = [getAvrColor()]
        points = 5
        degrees = 5
        for times in range(t):
            turnLeft(degrees)
            colors.append(getAvrColor)
        turnRight(t*degrees)
        print("Adding color {}\n".format(name))
        print("Outcome: {}\n".format(self.learnColorRight(colors.reverse, name)))
