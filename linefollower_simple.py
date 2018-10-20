from ev3dev.ev3 import *
from time   import sleep
from functools import reduce

#cl=ColorSensor()
on_dark=True
on_light=False


last_darks = []

#cl.mode='COL-REFLECT'
#left_motor=LargeMotor('outB')
#right_motor=LargeMotor('outA')

side_of_line = 1# 1 if left, -1 if right
speed = 300 * side_of_line


line_following_on = False


def follow_line():

    if (line_following_on):
        
        #on_light=cl.value()>40
        #on_dark=cl.value()<60
        print( "light: " + str(on_light) + ", dark: " + str(on_dark))
    
        if (on_dark):
            last_darks.append(True)
        elif (on_light):
            last_darks.append(False)
    
        if (reduce((lambda x,y: x and y),last_darks)):
            #turn right
            left_motor.run_timed(time_sp=100, speed_sp=-speed, stop_action='brake')
            right.run_timed(time_sp=100, speed_sp=speed, stop_action='brake')
            print("käänny oikealle")
        elif (reduce((lambda x,y: x and y), map((lambda x: not x), last_darks))):
            #turn left
            right_motor.run_timed(time_sp=100, speed_sp=-speed, stop_action='brake')
            left_motor.run_timed(time_sp=100, speed_sp=speed, stop_action='brake')
            print("käänny vasemmalle")
        elif(on_dark):
            #move right
            left_motor.run_timed(time_sp=100, speed_sp=-speed, stop_action='brake')
            print("liiku vasemmalle")
        elif(on_light):
            #move left
            right_motor.run_timed(time_sp=100, speed_sp=-speed, stop_action='brake')
            print("liiku oikealle")
    
        if (len(last_darks) > 4):
            last_darks.pop(0)
        print("kierros")
        sleep(0.1)    

print("start following")
line_following_on = True


while (True):
    follow_line()


