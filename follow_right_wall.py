import math
from turn_robot import *
from ev3dev.ev3 import *

class FollowRight:
    doneFlag = False
    driven = 0
    wallUvPadding = 30
    def __init__(self,left_motor,right_motor,touch_sensor_right,touch_sensor_left, uv_sensor):
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.touch_sensor_left=touch_sensor_left
        self.touch_sensor_right=touch_sensor_right
        self.un_sensor=uv_sensor

    def findWall(self):
        turn_right(left_motor, right_motor, 40)
        found = move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, uv_sensor, uvDist=38)
        
    def execute(self, stopAt):
        doneFlag = False
        while(doneFlag):

