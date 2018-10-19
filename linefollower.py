from ev3dev.ev3 import *
from time   import sleep

cl=ColorSensor()
on_dark=True
on_light=True

cl.mode='COL-REFLECT'
left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')
while(True):

    on_light=cl.value()>40
    on_dark=cl.value()<60

    if(on_dark):
        left_motor.run_timed(time_sp=200, speed_sp=900, stop_action='brake')
        print("vasen")
    if(on_light):
        right_motor.run_timed(time_sp=200, speed_sp=900, stop_action='brake')
        print("oikea")
    print("kierros")
    sleep(0.2)
