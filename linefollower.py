from ev3dev.ev3 import *

cl=ColorSensor()
on_dark=True
on_light=True

cl.mode='COL-REFLECT'
while(True):
    left_motor=Motor('OutB')
    right_motor=Motor('OutA')
    on_light=cl.value()>40
    on_dark=cl.value()<60

    if(on_dark):
        left_motor.run_timed(time_sp=200, speed_sp=900, stop_action='brake')
    if(on_light):
        right_motor.run_timed(time_sp=200, speed_sp=900, stop_action='brake')
    left_motor.wait_while('running')
    right_motor.wait_while('running')
    sleep(0.2)
