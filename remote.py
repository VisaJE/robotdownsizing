from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce
from math import *
from block_solver import *
from pylvas import *
import curses
from linefollower_simple import Linefollower
from ColorStuff import ColorStuff
from solve_pyor import Pyoriva
from turn_robot import *

class Remote:
    def __init__(self, cs):
        self.colorS = ColorStuff(cs)
        self.lm = LargeMotor('outB')
        self.rm = LargeMotor('outA')
        self.mm = Motor('outC')
        self.touch_sensor_right=TouchSensor('in2')
        self.touch_sensor_left=TouchSensor('in3')
        self.cs = cs
        self.line_follower=Linefollower(self.cs, self.lm, self.rm,self.touch_sensor_left, self.touch_sensor_right)
    def inputLoop(self):
        print("remote start")
        inp = ''

        while inp != 'q':
            inp = input()
            if inp == 'a':
                self.rm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 's':
                self.lm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
                self.rm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
            elif inp == 'd':
                self.lm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 'w':
                self.lm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
                self.rm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 'j':
                self.rm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
            elif inp == 'k':
                self.lm.run_timed(time_sp=250, speed_sp=900, stop_action='brake')
                self.rm.run_timed(time_sp=250, speed_sp=900, stop_action='brake')
            elif inp == 'l':
                self.lm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
            elif inp == 'i':
                self.lm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
                self.rm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
            elif inp == 'r':
                self.mm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 't':
                self.mm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
            elif inp == 'pylvas':
                position=[75,0]
                preferred=[[75,10],[130,45], [75,70], [135,130], [130,160], [75,160], [75, 180]]
                solver=Pylvas_solver(self.lm,self.rm,self.touch_sensor_right,self.touch_sensor_left,position,preferred)
                solver.execute()
            elif inp == 'block1':
                solver=Block_solver(self.lm,self.rm,self.touch_sensor_right,self.touch_sensor_left)
                solver.execute1()
            elif inp == 'block2':
                solver=Block_solver(self.lm,self.rm,self.touch_sensor_right,self.touch_sensor_left)
                solver.execute2()
            elif inp == 'perkele':
                Sound.speak('p e r r k e l e').wait
            elif inp == 'follow':
                stop=input()
                self.line_follower.start(self.colorS, stop_color=stop)
            elif inp == 'pyori':
                pp = Pyoriva()
                pp.run()
            elif inp == 'learn':
                name=input()
                self.colorS.learnColor(name)
            elif inp == 'forward':
                dist = int(input())
                move(self.lm, self.rm, self.touch_sensor_left, self.touch_sensor_right, dist)
            elif inp=='backwards':
                dist = int(input())
                move_backwards(self.lm, self.rm, distance=dist)
            elif inp=='left':
                angle=int(input())
                turn_left(self.lm, self.rm,degrees=angle)
            elif inp=='right':
                angle=int(input())
                turn_right(self.lm, self.rm, degrees=angle)
            sleep(0.25)
        print("remote exit")
