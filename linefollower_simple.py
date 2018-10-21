from ev3dev.ev3 import *
from time   import sleep
from functools import reduce
from turn_robot import *


class Linefollower:
    
    def __init__(self, cs):
        self.cl=cs.cl
        self.left_motor=LargeMotor('outB')
        self.right_motor=LargeMotor('outA')
        self.touch_sensor_left=TouchSensor('in3')
        self.touch_sensor_right=TouchSensor('in2')
        self.cs = cs
        self.line_following_on = True


        self.speed = int(input("SPEED: "))
        self.run_time = int(input("RUNTIME: "))
        self.buffer_size = int(input("BUFFERSIZE: "))
        self.on_dark=True
        self.on_light=False
        self.mode='COL-REFLECT'
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
                move(self.left_motor, self.right_motor, self.touch_sensor_left, self.touch_sensor_right, distance=7)
                turn_right(self.left_motor, self.right_motor,degrees=70)
                #turn right
                #left_motor.run_timed(time_sp=, speed_sp = -self.speed, stop_action='brake')
                #right_motor.run_timed(time_sp=, speed_sp = -self.speed, stop_action='brake')
                #left_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                #right_motor.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
                
            elif (turnleft):
                self.right_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                self.left_motor.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
            
            elif(moveright):
                 self.left_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                 self.right_motor.run_timed(time_sp=self.run_time, speed_sp=-0.3*self.speed, stop_action='brake')
            
            elif(moveleft): 
                self.right_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                
                self.left_motor.run_timed(time_sp=self.run_time, speed_sp=-0.3*self.speed, stop_action='brake')
                #print("liiku oikealle")
    
            if (self.touch_sensor_left.is_pressed or self.touch_sensor_right.is_pressed):
                print("COLLISION! MOVING BACKWARDS")
                Sound.speak('Perkele',espeak_opts='-a 200 -v finnish').wait()
                move_backwards(self.left_motor, self.right_motor,distance=3)
    
            if (len(self.last_darks) > self.buffer_size):
                self.last_darks.pop(0)
            #print("kierros")
            sleep(self.run_time/1000)     

    def lineLoop(self):
        while(self.cs.getColorFUCK()[0] != 'changeRed'):
            self.follow_line()





