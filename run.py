import math
from turn_robot import *
from ev3dev.ev3 import *
from pylvas import *
lm = LargeMotor('outB')
rm = LargeMotor('outA')
touch_sensor_right=TouchSensor('in2')
touch_sensor_left=TouchSensor('in3')
solver=Pylvas_solver(lm,rm,touch_sensor_right,touch_sensor_left)
solver.execute()
