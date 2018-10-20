import ev3dev.auto
from ColorStuff.py import *

print("Starting tests.\n")
print("Avr color here: {}\n".format(getAvrColor))
print("Learning a color.\n")
res = findColorFromRight('test')
if res:
    print("Found a color! {}\n".format(knownColors['test']))
else:
    print("Failed!\n")
