from ev3dev.ev3 import *
from time   import sleep
from collections import namedtuple
from functools import reduce
from math import *

class Remote:
    def __init__(self):
        lm = LargeMotor('outB')
        rm = LargeMotor('outA')
    def inputLoop(self):
        while True:
            inp = input("")
            if inp == 'q':
                break
            if inp == 'a':
                lm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
            elif inp == 's':
                lm.run_timed(time_sp=250, speed_sp=300, stop_action='brake')
                rm.run_timed(time_sp=250, speed_sp=300, stop_action='brake')
            elif inp == 'd':
                rm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
            elif inp == 'w':
                lm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
                rm.run_timed(time_sp=250, speed_sp=-300, stop_action='brake')
            sleep(0.25)