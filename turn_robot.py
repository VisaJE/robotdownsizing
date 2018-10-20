def turn(degrees=90):
    c=10
    if(degrees>0):
        left_motor.run_forever(speed_sp=-900,time_sp=c*degrees,stop_action='brake')
        right_motor.run_forever(speed_sp=900,time_sp=c*degrees,stop_action='brake')
    else:
        left_motor.run_forever(speed_sp=900,time_sp=c*degrees,stop_action='brake')
        right_motor.run_forever(speed_sp=-900,time_sp=c*degrees,stop_action='brake')

left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')
