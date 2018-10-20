import math
from turn_robot import *
from ev3dev.ev3 import *
from pylvas import *
lm = LargeMotor('outB')
rm = LargeMotor('outA')
touch_sensor_right=TouchSensor('in2')
touch_sensor_left=TouchSensor('in3')
position=[75,0]
preferred=[[75,20],[130,35], [135,50], [75,70], [75,75], [135,110], [130,135], [75,140], [75, 170]]
solver=Pylvas_solver(lm,rm,touch_sensor_right,touch_sensor_left,position,preferred)
solver.execute()
