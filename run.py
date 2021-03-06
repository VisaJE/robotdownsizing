import math
from turn_robot import *
from ev3dev.ev3 import *
from pylvas import *
lm = LargeMotor('outB')
rm = LargeMotor('outA')
touch_sensor_right=TouchSensor('in2')
touch_sensor_left=TouchSensor('in3')
position=[75,-20]
preferred=[[75,10],[130,45], [75,70], [135,140], [130,160], [75,160], [75, 180]]
solver=Pylvas_solver(lm,rm,touch_sensor_right,touch_sensor_left,position,preferred)
solver.execute()
