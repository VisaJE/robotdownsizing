from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff

#lm = LargeMotor('outB')
#rm = LargeMotor('outA')

tsl = TouchSensor('in4')
tsr = TouchSensor('in2')

cs = ColorStuff()

print(cs.getColor()[0])