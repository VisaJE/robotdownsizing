from ev3dev.ev3 import *
from time import sleep
from ColorStuff import ColorStuff
from remote import Remote

lm = LargeMotor('outB')
rm = LargeMotor('outA')

tsl = TouchSensor('in4')
tsr = TouchSensor('in2')

cs = ColorStuff()
us = UltrasonicSensor() 

us.mode='US-DIST-CM'
state = 0
colors = []

rem = Remote(cs)
rem.inputLoop()
while True:
	print("statte " + str(state))
	color = cs.getColorFUCK()[0]
	print("color " + color)
	colors += color
	distance = us.value()
	print("dist " + str(distance))
	input("Press Enter to continue...")
	if tsr.value():
		state = 1
	if tsl.value():
		state = 5
	if cs.getColorFUCK()[0] == 'changeRed':
		state = 4
	if state >= 4 and cs.getColorFUCK()[0] == 'ground' and len(colors) > 2 and colors[len(colors)-2] == 'ground':
		print("DONE")
		quit()
	if state == 0:
		lm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
	elif state == 1: #hit wall on right
		lm.run_timed(time_sp=250, speed_sp=400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=400, stop_action='brake')
		state = 2
	elif state == 2:#correct hit wall on right
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		state = 3
	elif state == 3:
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		lm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
	elif state == 4:
		lm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
	elif state == 5:#hit wall on left
		lm.run_timed(time_sp=250, speed_sp=400, stop_action='brake')
		rm.run_timed(time_sp=250, speed_sp=400, stop_action='brake')
		state = 6
	elif state == 6:#correct hit wall on left
		lm.run_timed(time_sp=250, speed_sp=-400, stop_action='brake')
		state = 3
	

	sleep(0.3)
