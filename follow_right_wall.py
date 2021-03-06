import math
from turn_robot import *
from ev3dev.ev3 import *

class FollowRight:
    doneFlag = False
    driven = 0
    wallUsPadding = 70
    def __init__(self,left_motor,right_motor,touch_sensor_right,touch_sensor_left, us_sensor):
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.touch_sensor_left=touch_sensor_left
        self.touch_sensor_right=touch_sensor_right
        self.us_sensor=us_sensor

    def initial_turn(self):
        print("Turning towards a wall")
        turn_right(self.left_motor, self.right_motor, 40)

    def findWall(self):
        print("Finding wall")
        found = moveWithUS(self.left_motor, self.right_motor, self.touch_sensor_left, self.touch_sensor_right, self.us_sensor, distance=40, usDist=self.wallUsPadding)
        self.driven += found[0]
        print('Us now {}'.format(self.us_sensor.value()))
        if found[0]+3 >= self.driven:
            print("Not found yet")
            self.initial_turn()
            self.findWall()
        elif found[1]:
            print("Left hit")
            move_backwards(self.left_motor, self.right_motor, 4)
            turn_left(self.left_motor, self.right_motor, 70)
        elif found[2]:
            print("right hit")
            move_backwards(self.left_motor, self.right_motor, 2)
            turn_left(self.left_motor, self.right_motor, 20)
        elif found[3] <= self.wallUsPadding:
            print("Us dist reached")
            move_backwards(self.left_motor, self.right_motor, 4)
            turn_left(self.left_motor, self.right_motor, 45)
        else:
            return False
        return True
    
    def checkStopFlag(self, stopAt, stopValue):
        if (stopAt == 'distance'):
            print('Stopping at distance {}'.format(stopAt))
            print('driven')
            if self.driven >= stopValue:
                self.doneFlag = True

    def checkWall(self):
        print('Checking if wall is here')
        turn_right(self.left_motor, self.right_motor, 90)
        if us_sensor.value() > wallUsPadding:
            res = moveWithUS(self.left_motor,self.right_motor, self.touch_sensor_left, self.touch_sensor_right, self.us_sensor, distance=us_sensor.value()-wallUsPadding, usDist=self.wallUsPadding)
            self.driven += res[0]
            if (res[1] or res[2]):
                turn_left(self.left_motor, self.right_motor, 70)
            else:
                return
        else:
            turn_left(self.left_motor, self.right_motor, 90)

    def execute(self, stopAt, stopValue):
        print("Executing")
        self.doneFlag = False
        self.initial_turn()
        self.findWall()
        while(not self.doneFlag):
            step = moveWithUS(self.left_motor, self.right_motor, self.touch_sensor_left, self.touch_sensor_right, self.us_sensor, distance=20, usDist=self.wallUsPadding)
            self.driven += step[0]
            self.checkStopFlag(stopAt, stopValue)
            if (not self.doneFlag):
                self.checkWall()
