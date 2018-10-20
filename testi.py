from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff
from turn_robot import *

cs = ColorStuff()
us = UltrasonicSensor() 
lm = LargeMotor('outB')
rm = LargeMotor('outA')
touch_sensor_right=TouchSensor('in2')
touch_sensor_left=TouchSensor('in3')

us.mode='US-DIST-CM'
state = 0
turn_right(lm, rm, 45)
sleep(5)
turn_left(lm, rm, 45)
sleep(5)
turn_right(lm, rm, 90)
sleep(5)
turn_left(lm, rm, 180)
sleep(5)
move(lm, rm, touch_sensor_left, touch_sensor_right, distance=10)

