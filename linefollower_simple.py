from ev3dev.ev3 import *
from time   import sleep
from functools import reduce
cl=ColorSensor()
on_dark=True
on_light=True

last_darks = []

cl.mode='COL-REFLECT'
left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')
while(True):

    on_light=cl.value()>40
    on_dark=cl.value()<60
    print("cl " + str(cl.value()) + " " + str(on_light) + " "+str(on_dark))
    
    if (on_dark):
        last_darks.append(True)
    else if (on_light):
        last_darks.append(False)
    
    if (reduce((lambda x,y: x and y),last_darks)):
        #turn right
        left_motor.run_timed(time_sp=100, speed_sp=-300, stop_action='brake')
        right.run_timed(time_sp=100, speed_sp=300, stop_action='brake')
    else if (reduce((lambda x,y: x and y),last_darks)):
        #turn left
        right_motor.run_timed(time_sp=100, speed_sp=-300, stop_action='brake')
        left_motor.run_timed(time_sp=100, speed_sp=300, stop_action='brake')
    else if(on_dark):
        #move right
        left_motor.run_timed(time_sp=100, speed_sp=-300, stop_action='brake')
        print("vasen")
    else if(on_light):
        #move left
        right_motor.run_timed(time_sp=100, speed_sp=-300, stop_action='brake')
        print("oikea")
    
    if (len(last_darks) > 4):
        last_darks.pop(0)
    print("kierros")
    sleep(0.1)
