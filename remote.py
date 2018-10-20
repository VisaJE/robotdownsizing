from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce
from math import *
import curses

class Remote:
    def __init__(self):
        self.lm = LargeMotor('outB')
        self.rm = LargeMotor('outA')
        self.mm = Motor('outC')
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
            sleep(0.25)
        print("remote exit")