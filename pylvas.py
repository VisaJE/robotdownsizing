import math
from turn_robot import *
from ev3dev.ev3 import *

class Pylvas_solver:
    not_done=True
    orientation=90
    stage=0
    last_moves=0
    bumped_left=False
    bumped_right=False
    def __init__(self,left_motor,right_motor,touch_sensor_right,touch_sensor_left,position,preferred):
        self.preferred=preferred
        self.position=position
        self.position=position
        self.left_motor=left_motor
        self.right_motor=right_motor
        self.touch_sensor_left=touch_sensor_left
        self.touch_sensor_right=touch_sensor_right

    def execute(self):
        while self.not_done:
            while self.step_forward():
                pass
            if self.calculate_distance() > 10:
                self.fix_orientation()
            else:
                self.fix_position()
        return True

    def step_forward(self):
        if(self.stage==len(self.preferred)):
            self.not_done=False
        orientation_change=self.find_orientation()
        self.orientation-=orientation_change
        print("Orientation change: ", orientation_change)
        if orientation_change<0 :
            turn_left(self.left_motor,self.right_motor,orientation_change)
        else:
            turn_right(self.left_motor,self.right_motor,orientation_change)
        desired_dist=self.calculate_distance()
        self.last_moves,bump_l,bump_r=move(self.left_motor,self.right_motor, self.touch_sensor_left, self.touch_sensor_right,desired_dist)

        self.position[0]+=math.cos(self.orientation/360*2*math.pi)*self.last_moves
        self.position[1]+=math.sin(self.orientation/360*2*math.pi)*self.last_moves

        if bump_l:
            self.bumped_left=True
            #print("bumped left")
            return False
        if bump_r:
            self.bumped_right=True
            #print("bumped right")
            return False

        #self.position=self.preferred[self.stage]
        self.stage+=1
        if self.stage == len(self.preferred):
            self.not_done = False
        return True

    def fix_orientation(self):
        dist=10
        move_backwards(self.left_motor,self.right_motor, distance =dist)
        degree = 10
        if self.bumped_right:
            turn_left(self.left_motor,self.right_motor,degree)
            self.orientation-=degree
        elif self.bumped_left:
            turn_right(self.left_motor,self.right_motor,degree)
            self.orientation+=degree
        self.bumped_left=False
        self.bumped_right=False
        self.position[0]-=math.cos(self.orientation/360*2*math.pi)*dist
        self.position[1]-=math.sin(self.orientation/360*2*math.pi)*dist
        print("Position: ", self.position)
        return

    def fix_position(self):
        self.bumped_left=False
        self.bumped_right=False
        self.stage += 1
        return

    def find_orientation(self):
        if self.position[0]-self.preferred[self.stage][0]==0:
            tmp_or=math.pi/2
        else:
            tmp_or=math.atan2(self.preferred[self.stage][1] - self.position[1], self.preferred[self.stage][0] - self.position[0])
        indegs=self.orientation-tmp_or/2/math.pi*360
        return indegs

    def calculate_distance(self):
        return math.sqrt(math.pow(self.position[1]-self.preferred[self.stage][1],2)+math.pow(self.position[0]-self.preferred[self.stage][0],2))
