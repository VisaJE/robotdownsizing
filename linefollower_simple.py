from ev3dev.ev3 import *
from time   import sleep
from functools import reduce
from turn_robot import *


class Linefollower:
    
    def __init__(self, cl, left_motor, right_motor, touch_sensor_left, touch_sensor_right):
        self.on_dark=True
        self.on_light=False
        cl.mode='COL-REFLECT'
        self.last_darks = []
        
        self.side_of_line = False # False if right, True if left
        self.speed = 200
        self.run_time = 50
        self.buffer_size = 4
        self.line_following_on = False
    
    def follow_line(self):
    
        if (self.line_following_on):
        
            self.on_light=cl.value()>=25
            self.on_dark=cl.value()<25
            print(cl.value())
    
            if (self.on_dark):
                self.last_darks.append(True)
            elif (self.on_light):
                self.last_darks.append(False)
    
            turnright = (reduce((lambda x,y: x and y),self.last_darks) and self.side_of_line) or (reduce((lambda x,y: x and y), map((lambda x: not x), self.last_darks)) and not self.side_of_line) 
            turnleft = (reduce((lambda x,y: x and y),self.last_darks) and not self.side_of_line) or (reduce((lambda x,y: x and y), map((lambda x: not x), self.last_darks)) and self.side_of_line)
            
            moveright = (self.on_dark and self.side_of_line) or (self.on_light and not self.side_of_line)
            moveleft = (self.on_light and self.side_of_line) or (self.on_dark and not self.side_of_line)
    
            if (turnright):
                move(left_motor, right_motor, touch_sensor_left, touch_sensor_right, distance=10)
                turn_right(left_motor, right_motor,degrees=90)
                #turn right
                #left_motor.run_timed(time_sp=, speed_sp = -self.speed, stop_action='brake')
                #right_motor.run_timed(time_sp=, speed_sp = -self.speed, stop_action='brake')
                #left_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                #right_motor.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
                
            elif (turnleft):
                right_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                left_motor.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
            
            elif(moveright):
                 left_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                 right_motor.run_timed(time_sp=self.run_time, speed_sp=0.3*self.speed, stop_action='brake')
            
            elif(moveleft): 
                right_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                
                 left_motor.run_timed(time_sp=self.run_time, speed_sp=0.3*self.speed, stop_action='brake')
                #print("liiku oikealle")
    
            if (touch_sensor_left.is_pressed or touch_sensor_right.is_pressed):
                print("COLLISION! MOVING BACKWARDS")
                move_backwards(left_motor, right_motor)
    
            if (len(self.last_darks) > self.buffer_size):
                self.last_darks.pop(0)
            #print("kierros")
            sleep(self.run_time/1000)            


         

cl=ColorSensor()

left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')
touch_sensor_left=TouchSensor('in3')
touch_sensor_right=TouchSensor('in2')
lf = Linefollower(cl, left_motor, right_motor,touch_sensor_left, touch_sensor_right)
lf.line_following_on = True


lf.speed = int(input("SPEED: "))
lf.run_time = int(input("RUNTIME: "))
lf.buffer_size = int(input("BUFFERSIZE: "))

while(True):
    lf.follow_line()







