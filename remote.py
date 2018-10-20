from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce
from math import *

class Remote:
    def __init__(self):
        self.lm = LargeMotor('outB')
        self.rm = LargeMotor('outA')
    def inputLoop(self):
        print("remote start")
        while True:
            inp = input("")
            if inp == 'q':
                break
            if inp == 'a':
                self.lm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
            elif inp == 's':
                self.lm.run_timed(time_sp=250, speed_sp=300, stop_action='brake')
                self.rm.run_timed(time_sp=250, speed_sp=300, stop_action='brake')
            elif inp == 'd':
                self.rm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
            elif inp == 'w':
                self.lm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
                self.rm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
            sleep(0.25)
        print("remote exit")