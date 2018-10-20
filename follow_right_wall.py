import math
from turn_robot import *
from ev3dev.ev3 import *

class FollowRight:
    doneFlag = False
    driven = 0
    wallUvPadding = 20
    def __init__(self,left_motor,right_motor,touch_sensor_right,touch_sensor_left, uv_sensor):
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.touch_sensor_left=touch_sensor_left
        self.touch_sensor_right=touch_sensor_right
        self.un_sensor=uv_sensor

    def initial_turn(self):
        turn_right(self.left_motor, self.right_motor, 40)
    def findWall(self):
        print("Finding wall")
        found = moveWithUv(self.left_motor, self.right_motor, self.touch_sensor_left, self.touch_sensor_right, self.uv_sensor, distance=40, uvDist=wallUvPadding)
        driven += found[0]
        if found[0]+3 >= distance:
            print("Not found yet")
            initial_turn(self)
            findWall(self)
        elif found[1]:
            print("Left hit")
            move_backwards(self.left_motor, self.right_motor, 5)
            turn_left(self.left_motor, self.right_motor, 70)
        elif found[2]:
            print("right hit")
            move_backwards(self.left_motor, self.right_motor, 3)
            turn_left(self.left_motor, self.right_motor, 20)
        elif found[3] <= uvDist:
            print("Uv dist reached")
            move_backwards(self.left_motor, self.right_motor, 4)
            turn_left(self.left_motor, self.right_motor, 45)
        else:
            return False
        return True
    
    def checkStopFlag(self, stopAt):
        if (stopAt == 'distance'):
            print('Stopping at distance {}'.format(stopAt))
            print('driven')
            if driven >= stopValue:
                doneFlag = True

    def checkWall(self):
        print('Checking if wall is here')
        turn_right(self.left_motor, self.right_motor, 90)
        if uv_sensor.value() > wallUvPadding:
            res = moveWithUv(self.left_motor,self.right_motor, self.touch_sensor_left, self.touch_sensor_right, self.uv_sensor, distance=uv_sensor.value()-wallUvPadding, uvDist=wallUvPadding)
            driven += res[0]
            if (res[1] or res[2]):
                turn_left(self.left_motor, self.right_motor, 70)
            else:
                return
        else:
            turn_left(self.left_motor, self.right_motor, 90)

    def execute(self, stopAt, stopValue):
        print("Executing")
        doneFlag = False
        self.initial_turn()
        self.findWall()
        while(not doneFlag):
            step = moveUv(self.left_motor, self.right_motor, self.touch_sensor_left, self.touch_sensor_right, self.uv_sensor, distance=20, uvDist=wallUvPadding)
            distance += step[0]
            if (not doneFlag):
                self.checkWall()
