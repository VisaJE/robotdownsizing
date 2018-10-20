from ev3dev.ev3 import *
from time import sleep
import ColorStuff as cs

lm = LargeMotor('outB')
rm = LargeMotor('outA')

tsl = TouchSensor('in2')
tsr = TouchSensor('in3')