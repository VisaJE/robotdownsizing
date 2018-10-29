from ev3dev.ev3 import *
from time   import sleep

cl = ColorSensor() 


def isOnChangeRed():
	oldMode = cl.mode
	cl.mode='RGB-RAW'
	r = cl.value(0)
    g = cl.value(1)
    b = cl.value(2)
    if r >= 185 && r <= 200 && g >= 220 && g <= 240 && b >= 180 && b <= 240:
    	return True
   	return False

def osa1():
	while True:
		
		sleep(0.1)
