
cs = ColorStuff()
us = UltrasonicSensor() 

us.mode='US-DIST-CM'
state = 0
while True:
	print("statte " + str(state))
	print(cs.getColorFUCK()[0])

