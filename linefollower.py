from ev3dev.ev3 import *
from time import sleep


class LineFollower:

    def run(self):

        cs = ColorSensor();
        #us = UltrasonicSensor(); assert us.connected

        cs.mode = 'COL-REFLECT'
        #us.mode = 'US-DIST-CM'

        lm = LargeMotor('outB')
        rm = LargeMotor('outA')

        speed = 360/4
        dt = 500
        stop_action = "coast"

        Kp = 1
        Ki = 0
        Kd = 0

        integral = 0
        previous_error = 0

        target_value = cs.value()

        while True:


           # distance = us.value() // 10

            error = target_value - cs.value()
            integral += (error * dt)
            derivative = (error - previous_error) / dt



            u = (Kp * error) + (Ki * integral) + (Kd * derivative)

            if speed + abs(u) > 1000:
                if u >= 0:
                    u = 1000 - speed
                else:
                    u = speed - 1000

            if u >= 0:
                lm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
                sleep(dt / 1000)
            else:
                lm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
                rm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
                sleep(dt / 1000)

            previous_error = error

    def pause(self, pct=0.0, adj=0.01):
        while self.btn.right or self.btn.left:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER, pct)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER, pct)
            if (pct + adj) < 0.0 or (pct + adj) > 1.0:
                adj = adj * -1.0
            pct = pct + adj

        print("[Continue]")
        Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

if __name__ == "__main__":
    robot = LineFollower()
    robot.run()
