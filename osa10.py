from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff

#lm = LargeMotor('outB')
#rm = LargeMotor('outA')

tsl = TouchSensor('in4')
tsr = TouchSensor('in2')

cs = ColorStuff()
s = UltrasonicSensor() 

us.mode='US-DIST-CM'




while True:
	print(cs.getColorFUCK()[0])
	distance = us.value()
	print("dist " + str(distance))
	sleep(0.3)