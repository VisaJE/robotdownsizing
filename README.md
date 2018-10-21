# robotdownsizing

First mission is solved by linefollower_simple.py with a simple algorithm using the color sensor. For the other tasks we have a general algorithm, implemented mostly in turn_robot.py and pylvas.py that makes the robot more or less follow given coordinates with respect to a given starting position and orientation. The system also detects bumps into an obstacle, in which case the robot moves a bit backwards and tries to correct its orientation. In addition we have a remote control system to use the robot's motors using keyboard commands if (when) all else fails.
