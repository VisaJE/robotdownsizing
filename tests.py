from ev3dev.ev3 import *
from time   import sleep

cl=ColorSensor()

cl.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')
while True:    # Stop program by pressing touch sensor button
    print(colors[cl.value()])
    #Sound.speak(colors[cl.value()]).wait()
    sleep(0.5)
