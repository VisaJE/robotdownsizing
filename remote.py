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
    def __init__(fuck, cs):
        fuck.colorS = ColorStuff(cs)
        fuck.lm = LargeMotor('outB')
        fuck.rm = LargeMotor('outA')
        fuck.mm = Motor('outC')
        fuck.touch_sensor_right=TouchSensor('in2')
        fuck.touch_sensor_left=TouchSensor('in3')
        fuck.cs = cs
        fuck.line_follower=Linefollower(fuck.cs, fuck.lm, fuck.rm,fuck.touch_sensor_left, fuck.touch_sensor_right)
    def inputLoop(fuck):
        print("remote start")
        inp = ''

        while inp != 'q':
            inp = input()
            if inp == 'a':
                fuck.rm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 's':
                fuck.lm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
                fuck.rm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
            elif inp == 'd':
                fuck.lm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 'w':
                fuck.lm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
                fuck.rm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 'j':
                fuck.rm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
            elif inp == 'k':
                fuck.lm.run_timed(time_sp=250, speed_sp=900, stop_action='brake')
                fuck.rm.run_timed(time_sp=250, speed_sp=900, stop_action='brake')
            elif inp == 'l':
                fuck.lm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
            elif inp == 'i':
                fuck.lm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
                fuck.rm.run_timed(time_sp=250, speed_sp=-900, stop_action='brake')
            elif inp == 'r':
                fuck.mm.run_timed(time_sp=250, speed_sp=-450, stop_action='brake')
            elif inp == 't':
                fuck.mm.run_timed(time_sp=250, speed_sp=450, stop_action='brake')
            elif inp == 'pylvas':
                position=[75,0]
                preferred=[[75,10],[130,45], [75,70], [135,130], [130,160], [75,160], [75, 180]]
                solver=Pylvas_solver(fuck.lm,fuck.rm,fuck.touch_sensor_right,fuck.touch_sensor_left,position,preferred)
                solver.execute()
            elif inp == 'block1':
                solver=Block_solver(fuck.lm,fuck.rm,fuck.touch_sensor_right,fuck.touch_sensor_left)
                solver.execute1()
            elif inp == 'block2':
                solver=Block_solver(fuck.lm,fuck.rm,fuck.touch_sensor_right,fuck.touch_sensor_left)
                solver.execute2()
            elif inp == 'perkele':
                Sound.speak('p e r r k e l e').wait
            elif inp == 'follow':
                stop=input()
                fuck.line_follower.start(fuck.colorS, stop_color=stop)
            elif inp == 'pyori':
                pp = Pyoriva()
                pp.run()
            elif inp == 'learn':
                name=input()
                fuck.colorS.learnColor(name)
            elif inp == 'forward':
                dist = int(input())
                move(fuck.lm, fuck.rm, fuck.touch_sensor_left, fuck.touch_sensor_right, dist)
            elif inp=='backwards':
                dist = int(input())
                move_backwards(fuck.lm, fuck.rm, distance=dist)
            elif inp=='left':
                angle=int(input())
                turn_left(fuck.lm, fuck.rm,degrees=angle)
            elif inp=='right':
                angle=int(input())
                turn_right(fuck.lm, fuck.rm, degrees=angle)
            sleep(0.25)
        print("remote exit")
