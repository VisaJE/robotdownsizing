from ev3dev.ev3 import *
from time   import sleep
from functools import reduce
from turn_robot import *


class Linefollower:
    
    def __init__(fuck, cl, left_motor, right_motor, touch_sensor_left, touch_sensor_right):
        fuck.on_dark=True
        fuck.on_light=False
        cl.mode='COL-REFLECT'
<<<<<<< HEAD
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.touch_sensor_left = touch_sensor_left
        self.touch_sensor_right = touch_sensor_right
        self.last_darks = []
<<<<<<< HEAD
        self.cl = cl
=======
        self.left_motor = left_motor
        self.touch_sensor_left = touch_sensor_left
        self.touch_sensor_right = touch_sensor_right
>>>>>>> vittu
        self.side_of_line = False # False if right, True if left
        self.speed = 200
        self.run_time = 50
        self.buffer_size = 4
        self.line_following_on = False
=======
        fuck.left_motor = left_motor
        fuck.right_motor = right_motor
        fuck.touch_sensor_left = touch_sensor_left
        fuck.touch_sensor_right = touch_sensor_right
        fuck.last_darks = []
        fuck.cl = cl
        fuck.side_of_line = False # False if right, True if left
        fuck.speed = 200
        fuck.run_time = 50
        fuck.buffer_size = 4
        fuck.line_following_on = False
>>>>>>> Automated message, ignore
    
    def follow_line(fuck):
    
        if (fuck.line_following_on):
        
            fuck.on_light=fuck.cl.value()>=25
            fuck.on_dark=fuck.cl.value()<25
            print(fuck.cl.value())
    
            if (fuck.on_dark):
                fuck.last_darks.append(True)
            elif (fuck.on_light):
                fuck.last_darks.append(False)
    
            turnright = (reduce((lambda x,y: x and y),fuck.last_darks) and fuck.side_of_line) or (reduce((lambda x,y: x and y), map((lambda x: not x), fuck.last_darks)) and not fuck.side_of_line) 
            turnleft = (reduce((lambda x,y: x and y),fuck.last_darks) and not fuck.side_of_line) or (reduce((lambda x,y: x and y), map((lambda x: not x), fuck.last_darks)) and fuck.side_of_line)
            
            moveright = (fuck.on_dark and fuck.side_of_line) or (fuck.on_light and not fuck.side_of_line)
            moveleft = (fuck.on_light and fuck.side_of_line) or (fuck.on_dark and not fuck.side_of_line)
    
            if (turnright):
                move(fuck.left_motor, fuck.right_motor, fuck.touch_sensor_left, fuck.touch_sensor_right, distance=7)
                turn_right(fuck.left_motor, fuck.right_motor,degrees=60)
                #turn right
<<<<<<< HEAD
                #self.left_motor.run_timed(time_sp=, speed_sp = -self.speed, stop_action='brake')
                #self.right_motor.run_timed(time_sp=, speed_sp = -self.speed, stop_action='brake')
                #self.left_motor.run_timed(time_sp=self.run_time, speed_sp=-self.speed, stop_action='brake')
                #self.right_motor.run_timed(time_sp=self.run_time, speed_sp=self.speed, stop_action='brake')
=======
                #left_motor.run_timed(time_sp=, speed_sp = -fuck.speed, stop_action='brake')
                #right_motor.run_timed(time_sp=, speed_sp = -fuck.speed, stop_action='brake')
                #left_motor.run_timed(time_sp=fuck.run_time, speed_sp=-fuck.speed, stop_action='brake')
                #right_motor.run_timed(time_sp=fuck.run_time, speed_sp=fuck.speed, stop_action='brake')
>>>>>>> Automated message, ignore
                
            elif (turnleft):
                fuck.right_motor.run_timed(time_sp=fuck.run_time, speed_sp=-fuck.speed, stop_action='brake')
                fuck.left_motor.run_timed(time_sp=fuck.run_time, speed_sp=fuck.speed, stop_action='brake')
            
            elif(moveright):
                 fuck.left_motor.run_timed(time_sp=fuck.run_time, speed_sp=-fuck.speed, stop_action='brake')
                 fuck.right_motor.run_timed(time_sp=fuck.run_time, speed_sp=-0.3*fuck.speed, stop_action='brake')
            
            elif(moveleft): 
                fuck.right_motor.run_timed(time_sp=fuck.run_time, speed_sp=-fuck.speed, stop_action='brake')
                
                fuck.left_motor.run_timed(time_sp=fuck.run_time, speed_sp=-0.3*fuck.speed, stop_action='brake')

                #print("liiku oikealle")
    
            if (fuck.touch_sensor_left.is_pressed or fuck.touch_sensor_right.is_pressed):
                print("COLLISION! MOVING BACKWARDS")
                #Sound.speak('Perkele',espeak_opts='-a 200 -v finnish').wait()
                move_backwards(fuck.left_motor, fuck.right_motor,distance=5)
                if (fuck.touch_sensor_right.is_pressed):
                    move_backwards(fuck.left_motor, fuck.right_motor,distance=5)
                    fuck.right_motor.run_timed(time_sp=fuck.run_time, speed_sp=-fuck.speed, stop_action='brake')
                    sleep(fuck.run_time/1000)
                    fuck.right_motor.run_timed(time_sp=3*fuck.run_time, speed_sp=fuck.speed, stop_action='brake')
                    fuck.left_motor.run_timed(time_sp=3*fuck.run_time, speed_sp=fuck.speed, stop_action='brake')
                    sleep(3*fuck.run_time/1000)
                else:
                    move_backwards(fuck.left_motor, fuck.right_motor,distance=5)
            if (len(fuck.last_darks) > fuck.buffer_size):
                fuck.last_darks.pop(0)
            #print("kierros")
            sleep(fuck.run_time/1000)            

    def start(fuck, color_stuff, stop_color='acasc'):
        fuck.speed = int(input("SPEED: "))
        fuck.run_time = int(input("RUNTIME: "))
        fuck.buffer_size = int(input("BUFFERSIZE: "))
        fuck.line_following_on=True
        doing=True
        try:
            while(doing):
                fuck.follow_line()
                if color_stuff.getColorFUCK() == stop_color:
                    if color_stuff.getAvrColorFUCK() == stop_color:
                        doing=False
        except KeyboardInterrupt:
            print("Interrupted")

"""
cl=ColorSensor()
self.left_motor=LargeMotor('outB')
self.right_motor=LargeMotor('outA')
self.touch_sensor_left=TouchSensor('in3')
self.touch_sensor_right=TouchSensor('in2')

lf = Linefollower(cl, self.left_motor, self.right_motor,self.touch_sensor_left, self.touch_sensor_right)
lf.line_following_on = True


lf.speed = int(input("SPEED: "))
lf.run_time = int(input("RUNTIME: "))
lf.buffer_size = int(input("BUFFERSIZE: "))

while(True):
    lf.follow_line()"""
