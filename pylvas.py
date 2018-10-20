import math
from turn_robot import *
from ev3dev.ev3 import *

class Pylvas_solver:
    not_done=True
    position=[75,0]
    orientation=90
    preferred=[[75,15],[90,25]]
    stage=0
    last_moves=0
    bumped_left=False
    bumped_right=False
    def __init__(self,left_motor,right_motor,touch_sensor_right,touch_sensor_left):
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.touch_sensor_left=touch_sensor_left
        self.touch_sensor_right=touch_sensor_right

    def execute(self):
        while not_done:
            while step_forward():
                pass
            step_backwards()
        return True

    def step_forward(self):
        orientation_change=find_orientation()
        if orientation_change>0 :
            turn_left(left_motor,right_motor,orientation_change)
        else:
            turn_right(left_motor,right_motor,-orientation_change)
        desired_dist=calculate_distance()
        self.last_move,bump_l,bump_r=move(left_motor,right_motor, touch_sensor_left, touch_sensor_right,desired_dist)
        if bump_l:
            self.bumped_left=True
            return False
        if bump_r:
            self.bumped_right=True
            return False
        position=preferred[stage]
        stage+=1
        return True

    def step_backwards(self):
        move_backwards(left_motor,right_motor, touch_sensor_left, touch_sensor_right, last_move)
        if bumped_right:
            turn_left(left_motor,right_motor,10)
        if bumped_left:
            turn_right(left_motor,right_motor,10)
        self.bumped_left=False
        self.bumped_right=False

    def find_orientation(self):
            tmp_or=math.atan((self.position[1]-self.preferred[stage][1])/(self.position[0]-self.preferred[stage][0]))
            indegs=self.orientation-tmp_or/2/math.Pi*360
            return indegs

    def calculate_distance(self):
        return math.sqrt(math.pow(self.position[1]-self.preferred[stage][1],2)+math.pow(self.position[0]-self.preferred[stage][0],2))
