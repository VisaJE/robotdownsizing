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

    def initial_turn(self):
        turn_right(left_motor, right_motor, 40)
    def findWall(self):
        found = move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, uv_sensor, distance=40, uvDist=wallUvPadding)
        driven += found[0]
        if found[0]+3 >= distance:
            initial_turn(self)
            findWall(self)
        elif found[1]:
            move_backwards(left_motor, right_motor, 5)
            turn_left(left_motor, right_motor, 70)
        elif found[2]:
            move_backwards(left_motor, right_motor, 3)
            turn_left(left_motor, right_motor, 20)
        elif found[3] <= uvDist:
            move_backwards(left_motor, right_motor, 4)
            turn_left(left_motor, right_motor, 45)
        else return False
        return True
    
    def checkStopFlag(self, stopAt):
        if (stopAt = 'distance'):
            if driven >= stopValue:
                doneFlag = True'

    def execute(self, stopAt, stopValue):
        doneFlag = False
        initial_turn(self)
        findWall(self)
        while(doneFlag):
            step = move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, uv_sensor, distance=15, uvDist=wallUvPadding)
            distance += step[0]

            
