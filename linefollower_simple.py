from ev3dev.ev3 import *
from time   import sleep
from functools import reduce


class Linefollower:
    
    def __init__(self, cl, left_motor, right_motor):
        self.on_dark=True
        self.on_light=False
        #cl.mode='COL-REFLECT'
        self.last_darks = []
        self.side_of_line = -1 # 1 if left, -1 if right
        self.speed = 200 * self.side_of_line
        self.run_time = 50
        self.buffer_size = 4
        self.line_following_on = False
    
    def follow_line(self):
    
        if (self.line_following_on):
        
            self.on_light=cl.value()>40
            self.on_dark=cl.value()<60
            print( "light: " + str(self.on_light) + ", dark: " + str(self.on_dark))
    
            if (self.on_dark):
                last_darks.append(True)
            elif (self.on_light):
                last_darks.append(False)
    
            if (reduce((lambda x,y: x and y),self.last_darks)):
                #turn right
                left_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
                right.run_timed(time_sp=run_time, speed_sp=speed, stop_action='brake')
                print("käänny oikealle")
            elif (reduce((lambda x,y: x and y), map((lambda x: not x), self.last_darks))):
                #turn left
                right_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
                left_motor.run_timed(time_sp=run_time, speed_sp=speed, stop_action='brake')
                print("käänny vasemmalle")
            elif(self.on_dark):
                #move right
                left_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
                print("liiku vasemmalle")
            elif(self.on_light):
                #move left
                right_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
                print("liiku oikealle")
    
            if (len(self.last_darks) > self.buffer_size):
                self.last_darks.pop(0)
            print("kierros")
            sleep(0.05)            


         

cl=ColorSensor()

left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')

lf = Linefollower(cl,left_motor, right_motor)
lf.line_following_on = True

while(True):
    lf.follow_line()

"""cl=ColorSensor()
on_dark=True
on_light=False


last_darks = []

cl.mode='COL-REFLECT'
left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')

side_of_line = -1 # 1 if left, -1 if right
speed = 200 * side_of_line
run_time = 50
buffer_size = 4
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
            left_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
            right.run_timed(time_sp=run_time, speed_sp=speed, stop_action='brake')
            print("käänny oikealle")
        elif (reduce((lambda x,y: x and y), map((lambda x: not x), last_darks))):
            #turn left
            right_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
            left_motor.run_timed(time_sp=run_time, speed_sp=speed, stop_action='brake')
            print("käänny vasemmalle")
        elif(on_dark):
            #move right
            left_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
            print("liiku vasemmalle")
        elif(on_light):
            #move left
            right_motor.run_timed(time_sp=run_time, speed_sp=-speed, stop_action='brake')
            print("liiku oikealle")
    
        if (len(last_darks) > buffer_size):
            last_darks.pop(0)
        print("kierros")
        sleep(0.05)    


speed = int(input("SPEED: "))
run_time = int(input("RUNTIME: "))
buffer_size = int(input("BUFFERSIZE: "))
line_following_on = True


while (True):
    follow_line()"""







