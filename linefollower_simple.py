from ev3dev.ev3 import *
from time   import sleep
from functools import reduce
from ColorStuff import ColorStuff

class Linefollower:
    
    def __init__(self, cl, lm, rm):
        self.on_dark=True
        self.on_light=False
        #cl.mode='COL-REFLECT'
        self.last_darks = [False, True]
        self.side_of_line = False # False if left, True if right
        self.speed = 600
        self.run_time = 50
        self.buffer_size = 12
        self.line_following_on = False
        self.lm = lm
        self.rm = rm
    
    def follow_line(self):
    
        if (self.line_following_on):
        
            self.on_light = cl.value()>=40
            self.on_dark = cl.value()<40
            print(cl.value())
            if (self.on_light):
                print("ON TAPE")
                self.last_darks.append(False)
            elif (self.on_dark):
                print("ON GROUND")
                self.last_darks.append(True)
                
            right_turn = (reduce((lambda x,y: x and y),self.last_darks) and self.side_of_line) or ( reduce((lambda x,y: x and y), map((lambda x: not x), self.last_darks )) and not self.side_of_line)
            
            left_turn = right_turn = (reduce((lambda x,y: x and y),self.last_darks) and not self.side_of_line) or ( reduce((lambda x,y: x and y), map((lambda x: not x), self.last_darks )) and self.side_of_line)
            
            move_right = (self.on_dark and self.side_of_line) or (self.on_light and not self.side_of_line)            
            move_left = (self.on_dark and not self.side_of_line) or (self.on_light and self.side_of_line)
            
            if (right_turn):
                self.lm.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                self.rm.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
            
            elif (left_turn):
                self.rm.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                self.lm.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
            
            elif(move_right):
                self.lm.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                self.rm.run_timed(time_sp=self.run_time, speed_sp=-0.5*self.speed, stop_action='brake')
            elif(move_left): 
                self.rm.run_timed(time_sp=self.run_time, speed_sp=-self.speed,stop_action='brake')
                self.lm.run_timed(time_sp=self.run_time, speed_sp=-0.5*self.speed, stop_action='brake')
            
                
            if (len(self.last_darks) > self.buffer_size):
                self.last_darks.pop(0)
            #print("kierros")
            sleep(self.run_time/1000)            


         
cs = ColorStuff()

cl=ColorSensor()

left_motor=LargeMotor('outB')
right_motor=LargeMotor('outA')

lf = Linefollower(cl, left_motor, right_motor)
lf.line_following_on = True


lf.speed = int(input("SPEED: "))
lf.run_time = int(input("RUNTIME: "))
lf.buffer_size = int(input("BUFFERSIZE: "))


#rampille
#mustalle

while (cs.getColorFUCK()[0] != 'dimRed'):
    lf.follow_line()
    
#pylväspaskaan







