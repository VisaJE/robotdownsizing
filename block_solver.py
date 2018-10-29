from pylvas import *

class Block_solver:

    def __init__(fuck,left_motor,right_motor,touch_sensor_right,touch_sensor_left):
        fuck.left_motor=left_motor
        fuck.right_motor=right_motor
        fuck.touch_sensor_left=touch_sensor_left
        fuck.touch_sensor_right=touch_sensor_right

    def execute1(fuck):
        start=[0,0]
        preferred=[[20,100],[70,170],[55,320]]
        solver1=Pylvas_solver(fuck.left_motor,fuck.right_motor,fuck.touch_sensor_right,fuck.touch_sensor_left,start,preferred)
        solver1.execute()

    def execute2(fuck):
        start=[0,0]
        preferred=[[20,-10],[20,-120]]
        solver2=Pylvas_solver(fuck.left_motor,fuck.right_motor,fuck.touch_sensor_right,fuck.touch_sensor_left,start,preferred)
        solver2.execute()
