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

class Pyoriva:
    def __init__(self):
        self.lm = LargeMotor('outB')
        self.rm = LargeMotor('outA')
    def run(self):
        try:
            self.lm.run_timed(time_sp=550, speed_sp=-900, stop_action='brake')
            self.rm.run_timed(time_sp=550, speed_sp=-900, stop_action='brake')
            sleep(7)
            self.lm.run_timed(time_sp=550, speed_sp=900, stop_action='brake')
            self.rm.run_timed(time_sp=550, speed_sp=900, stop_action='brake')
            sleep(13)
            self.lm.run_timed(time_sp=550, speed_sp=-900, stop_action='brake')
            self.rm.run_timed(time_sp=550, speed_sp=-900, stop_action='brake')
            sleep(13)
            self.lm.run_timed(time_sp=550, speed_sp=900, stop_action='brake')
            self.rm.run_timed(time_sp=550, speed_sp=900, stop_action='brake')
        except KeyboardInterrupt:
            print("Interrupted")
