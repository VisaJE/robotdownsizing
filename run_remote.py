from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff
from remote import Remote

cs = ColorSensor()

rem = Remote(cs)
rem.inputLoop()
