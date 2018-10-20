from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff

#lm = LargeMotor('outB')
#rm = LargeMotor('outA')

tsl = TouchSensor('in4')
tsr = TouchSensor('in2')

cs = ColorStuff()
us = UltrasonicSensor() 

us.mode='US-DIST-CM'

print(cs.getColor()[0])


while True:
	distance = us.value()

	sleep(0.3)