from ev3dev.ev3 import *
from time import sleep
import ColorStuff as cs

#lm = LargeMotor('outB')
#rm = LargeMotor('outA')

tsl = TouchSensor('in4')
tsr = TouchSensor('in2')

cs = ColorStuff()

print(cs.getColor()[0])