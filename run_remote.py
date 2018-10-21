from remote import *
from e3dev import *
from ColorStuff import ColorStuff


cs = ColorStuff()
remote=Remote(cs)
remote.inputLoop()
