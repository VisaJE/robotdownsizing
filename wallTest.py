from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff
from turn_robot import *

us = UltrasonicSensor() 
lm = LargeMotor('outB')
rm = LargeMotor('outA')
tsr=TouchSensor('in2')
tsl=TouchSensor('in3')

follower = FollowRight(lm, rm, tsl, tsr, us)
follower.execute()
