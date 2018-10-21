from remote import *
from e3dev.ev3 import *
from ColorStuff import ColorStuff


cs = ColorStuff()
remote=Remote(cs)
remote.inputLoop()
