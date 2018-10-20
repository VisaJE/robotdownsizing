import ev3dev.ev3 as ev3
from time import sleep

def turn_left(left_motor,right_motor,degrees=90):
    c=14
    b=0
    t=90*14-100
    s=45*14-50+20

    left_motor.run_timed(speed_sp=200,time_sp=s,stop_action='brake')
    right_motor.run_timed(speed_sp=-200,time_sp=s,stop_action='brake')


def turn_right(left_motor,right_motor,degrees=90):
    left_motor.run_timed(speed_sp=-200,time_sp=s,stop_action='brake')
    right_motor.run_timed(speed_sp=200,time_sp=s,stop_action='brake')



def move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance=10,speed=500):
    c = 10
    mov = 0
    bumped_right=False
    bumped_left=False
    epsilon = 0.1
    while (touch_sensor_left.is_pressed or touch_sensor_right.is_pressed) and mov < distance:
        if mov + epsilon < distance:
            left_motor.run_timed(speed_sp=speed, time_sp=c*epsilon, stop_action='brake')
            right_motor.run_timed(speed_sp=speed, time_sp=c*epsilon, stop_action='brake')
            mov += epsilon
        else:
            left_motor.run_timed(speed_sp=speed, time_sp=c*(distance-mov), stop_action='brake')
            right_motor.run_timed(speed_sp=speed, time_sp=c*(distance-mov), stop_action='brake')
            mov = distance
    bumped_right=touch_sensor_right.is_pressed
    bumped_left=touch_sensor_left.is_pressed
    return mov, bumped_left,bumped_right

def move_backwards(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance=10,speed=500):
    move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance,-speed)
