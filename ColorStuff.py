from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce

class ColorStuff:
    def __init__(self):
        self.cl = ColorSensor()
        RGBColor = namedtuple('RGBColor', 'r g b')
        self.knownColors = {'null': RGBColor(0, 0, 0), 'changeRed': RGBColor(190, 210, 270), 'ground': RGBColor(32, 50, 35), 'tape': RGBColor(160, 230, 210)}
        self.differenceThreshold = 40
    
    # Returns tuple (seen color name, is the color within the threshold)
    def getColor():
        return self.getColor(self.getColorH())

    def getColorH():
        oldMode = cl.mode
        cl.mode='RGB-RAW'
        r = cl.value(0)
        g = cl.value(1)
        b = cl.value(2)
        c1.mode = oldMode
        return RGBColor(r, g, b)

    def getDistance(color1, color2):
        return sqrt(pow(color1['r']-color2['r'], 2) + pow(color1['g']-color2['g'],2) + pow(color1['b']-color2['b'], 2))

    def getClosestKnown(color1):
        dists = zip(knownColors.items(), knownColors.items().map(lambda x: getDistance(color1, x[1])))
        return min(dists, key=lambda t: t[1])

    def getColor(color):
        found = self.getClosestKnown(color)
        return (found[0][0], found[1] < differenceThreshold)


    def learnColorRight(colors, name):
        trimLeft = colors.copy()
        trimRight = colors.copy()
        n = len(colors)
        trimRight[1] = reduce((lambda x, y: (x[0]* (y[0]*1.0/(n-1), x[1]* (y[1]*1.0/(n-1), x[2]* (y[2]*1.0/(n-1)))))))
        for ind in range(1, n-1):
            for i in ('r', 'g', 'b'):
                trimLeft[ind][i] = trimLeft[ind-1][i]*1.0*ind/(ind+1)+trimLeft[ind][i]*1.0/(ind+1)
                trimRight[ind+1][i] = (trimRight[ind][i]*(n-ind) - colors[ind][i])/(n-ind-1)
        trimLeft = range(n).map(lambda a: getDistance(trimLeft[a], trimRight[a]))
        trimLeft[0] = 0
        trimLeft[n-1] = 0
        found = max(zip(trimLeft, range(n)), key= lambda a: a[0])
        print("Found biggest difference in avr color at index {}\n".format(found))
        if trimLeft[found] > differenceThreshold:
            knownColors[name] = trimRight[found]
            return True
        else:
            return False

    def getAvrColor():
        color = getColorH()
        for i in range(9):
            sleep(0.1)
            newCol = getColorH()
            for c in ['r', 'g', 'b']:
                color[c] = color[c] + newCol[c]
        for c in ['r', 'g', 'b']:
            color[c] /= 10

    def findColorFromRight(name):
        colors = [getAvrColor()]
        points = 5
        degrees = 5
        for times in range(t):
            turnLeft(degrees)
            colors.append(getAvrColor)
        turnRight(t*degrees)
        print("Adding color {}\n".format(name))
        print("Outcome: {}\n".format(self.learnColorRight(colors.reverse, name)))
