def turn(left_motor,right_motor,degrees=90):
    c=10
    if(degrees>0):
        left_motor.run_timed(speed_sp=-900,time_sp=c*degrees,stop_action='brake')
        right_motor.run_timed(speed_sp=900,time_sp=c*degrees,stop_action='brake')
    else:
        left_motor.run_timed(speed_sp=900,time_sp=c*degrees,stop_action='brake')
        right_motor.run_timed(speed_sp=-900,time_sp=c*degrees,stop_action='brake')

left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')
turn(left_motor,right_motor)



def move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance=10):
    c = 10
    mov = 0
    epsilon = 0.1
    while ((touch_sensor_left.is_pressed or touch_sensor_right.is_pressed) and mov < distance):
        if (mov + epsilon < distance):
            left_motor.run_timed(speed_sp=500, time_sp=c*epsilon, stop_action='brake')
            right_motor.run_timed(speed_sp=500, time_sp=c*epsilon, stop_action='brake')
            mov += epsilon
        else:
            left_motor.run_timed(speed_sp=500, time_sp=c*(distance-mov), stop_action='brake')
            right_motor.run_timed(speed_sp=500, time_sp=c*(distance-mov), stop_action='brake')
            mov = distance
        
    return mov
        
        
