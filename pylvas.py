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
    def __init__(fuck,left_motor,right_motor,touch_sensor_right,touch_sensor_left,position,preferred):
        fuck.preferred=preferred
        fuck.position=position
        fuck.left_motor=left_motor
        fuck.right_motor=right_motor
        fuck.touch_sensor_left=touch_sensor_left
        fuck.touch_sensor_right=touch_sensor_right

    def execute(fuck):
        try:
            while fuck.not_done:
                while fuck.step_forward():
                    pass
                if fuck.calculate_distance() > 10:
                    fuck.fix_orientation()
                else:
                    fuck.fix_position()
            return True
        except KeyboardInterrupt:
           print("Interrupted") 

    def step_forward(fuck):
        if(fuck.stage==len(fuck.preferred)):
            fuck.not_done=False
        orientation_change=fuck.find_orientation()
        fuck.orientation-=orientation_change
        print("Orientation change: ", orientation_change)
        if orientation_change<0 :
            turn_left(fuck.left_motor,fuck.right_motor,orientation_change)
        else:
            turn_right(fuck.left_motor,fuck.right_motor,orientation_change)
        desired_dist=fuck.calculate_distance()
        fuck.last_moves,bump_l,bump_r=move(fuck.left_motor,fuck.right_motor, fuck.touch_sensor_left, fuck.touch_sensor_right,desired_dist)

        fuck.position[0]+=math.cos(fuck.orientation/360*2*math.pi)*fuck.last_moves
        fuck.position[1]+=math.sin(fuck.orientation/360*2*math.pi)*fuck.last_moves

        if bump_l:
            fuck.bumped_left=True
            #print("bumped left")
            return False
        if bump_r:
            fuck.bumped_right=True
            #print("bumped right")
            return False

        #fuck.position=fuck.preferred[fuck.stage]
        fuck.stage+=1
        if fuck.stage == len(fuck.preferred):
            fuck.not_done = False
        return True

    def fix_orientation(fuck):
        dist=10
        move_backwards(fuck.left_motor,fuck.right_motor, distance =dist)
        degree = 10
        if fuck.bumped_right:
            turn_left(fuck.left_motor,fuck.right_motor,degree)
            fuck.orientation-=degree
        elif fuck.bumped_left:
            turn_right(fuck.left_motor,fuck.right_motor,degree)
            fuck.orientation+=degree
        fuck.bumped_left=False
        fuck.bumped_right=False
        fuck.position[0]-=math.cos(fuck.orientation/360*2*math.pi)*dist
        fuck.position[1]-=math.sin(fuck.orientation/360*2*math.pi)*dist
        print("Position: ", fuck.position)
        return

    def fix_position(fuck):
        fuck.bumped_left=False
        fuck.bumped_right=False
        fuck.stage += 1
        return

    def find_orientation(fuck):
        if fuck.position[0]-fuck.preferred[fuck.stage][0]==0:
            tmp_or=math.pi/2
        else:
            tmp_or=math.atan2(fuck.preferred[fuck.stage][1] - fuck.position[1], fuck.preferred[fuck.stage][0] - fuck.position[0])
        indegs=fuck.orientation-tmp_or/2/math.pi*360
        return indegs

    def calculate_distance(fuck):
        return math.sqrt(math.pow(fuck.position[1]-fuck.preferred[fuck.stage][1],2)+math.pow(fuck.position[0]-fuck.preferred[fuck.stage][0],2))
