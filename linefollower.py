from ev3dev.ev3 import *
from time   import sleep
m = LargeMotor('outA')

m.run_forever(speed_sp=200)   # equivalent to power=20 in EV3-G
sleep(5)
m.stop(stop_action="coast")
sleep(4)

m.run_forever()
sleep(5)
m.stop()
sleep(4)