from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce
from math import *
from block_solver import *
from pylvas import *
import curses

class Remote:
    def __init__(self):
        self.lm = LargeMotor('outB')
        self.rm = LargeMotor('outA')
        self.mm = Motor('outC')
        self.touch_sensor_right=TouchSensor('in2')
        self.touch_sensor_left=TouchSensor('in3')
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
            elif inp == 'r':
                self.mm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 't':
                self.mm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
            elif inp == 'pylvas':
                position=[75,0]
                preferred=[[75,20],[130,25], [135,50], [75,70], [75,75], [135,95], [130,135], [75,140], [75, 170]]
                solver=Pylvas_solver(lm,rm,touch_sensor_right,touch_sensor_left,position,preferred)
                solver.execute()
            elif inp == 'block1':
                solver=Block_solver(lm,rm,touch_sensor_right,touch_sensor_left)
                solver.execute1()
            elif inp == 'block2':
                solver=Block_solver(lm,rm,touch_sensor_right,touch_sensor_left)
                solver.execute2()
            elif inp == 'perkele':
                Sound.speak('p e r r k e l e').wait
            sleep(0.25)
        print("remote exit")
