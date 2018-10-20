from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff

lm = LargeMotor('outB')
rm = LargeMotor('outA')

tsl = TouchSensor('in4')
tsr = TouchSensor('in2')

cs = ColorStuff()
us = UltrasonicSensor() 

us.mode='US-DIST-CM'
state = 0
while True:
	print(cs.getColorFUCK()[0])
	distance = us.value()
	print("dist " + str(distance))
	if tsr.value():
		state = 
	if cs.getColorFUCK()[0] == 'changeRed':
		state = 3
	if state > 3 && cs.getColorFUCK()[0] == 'ground':
		print("DONE")
		quit()
	if state == 0:
		lm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
	if state == 1:
		lm.run_timed(time_sp=250, speed_sp=400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=400, stop_action='brake')
		state = 2
	if state == 2:
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		state = 2
	if state == 3:
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		state = 4
	if state == 4:
		lm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
	

	sleep(0.3)