import ev3dev.ev3 as ev3
from time import sleep
import math

def turn_left(left_motor,right_motor,degrees=90, flag=1): # flag=1 turns left, -1 turns right
    time = 60+math.abs(degrees)*540/45
    left_motor.run_timed(speed_sp=flag*-200,time_sp=time,stop_action='brake')
    right_motor.run_timed(speed_sp=flag*200,time_sp=time,stop_action='brake')
    sleep(time/1000)
    return

def turn_right(left_motor,right_motor,degrees=90):
    turn_left(left_motor, right_motor, degrees, -1)
    return

def move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance=10,speed=500):
    c = 50
    mov = 0
    bumped_right=False
    bumped_left=False
    epsilon=1
    pseudo_distance=1.24*distance
    while (not (touch_sensor_left.is_pressed or touch_sensor_right.is_pressed)) and mov < pseudo_distance:
        if mov + epsilon < pseudo_distance:
            left_motor.run_timed(speed_sp=-speed, time_sp=c*epsilon)
            right_motor.run_timed(speed_sp=-speed, time_sp=c*epsilon)
            mov += epsilon
        else:
            left_motor.run_timed(speed_sp=-speed, time_sp=c*(pseudo_distance-mov))
            right_motor.run_timed(speed_sp=-speed, time_sp=c*(pseudo_distance-mov))
            mov = pseudo_distance
        sleep(c*epsilon/1000)
    bumped_right=touch_sensor_right.is_pressed
    bumped_left=touch_sensor_left.is_pressed
    return distance, bumped_left, bumped_right

def move_backwards(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance=10,speed=500):
    c = 50
    mov = 0
    epsilon = 1
    pseudo_distance = 1.24*distance
    while mov < pseudo_distance:
        if mov + epsilon < pseudo_distance:
            left_motor.run_timed(speed_sp=speed, time_sp=c*epsilon)
            right_motor.run_timed(speed_sp=speed, time_sp=c*epsilon)
            mov += epsilon
        else:
            left_motor.run_timed(speed_sp=speed, time_sp=c*(pseudo_distance-mov))
            right_motor.run_timed(speed_sp=speed, time_sp=c*(pseudo_distance-mov))
            mov = pseudo_distance
        sleep(c*epsilon/1000)
    return
