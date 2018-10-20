import math
from turn_robot import *
from ev3dev.ev3 import *
from pylvas import *
lm = LargeMotor('outB')
rm = LargeMotor('outA')
touch_sensor_right=TouchSensor('In2')
touch_sensor_left=TouchSensor('In4')
move(lm, rm, touch_sensor_left, touch_sensor_right, distance=10)
#solver=new Pylvas_solver(lm,rm,touch_sensor_right,touch_sensor_left)
#solver.execute()
