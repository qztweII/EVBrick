#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import random as r


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

MotorL = Motor(Port.B)
MotorR = Motor(Port.C)

while True:
    # Write your program here.
    Driver = DriveBase(MotorL, MotorR, wheel_diameter = 55, axle_track = 104)
    for i in range(10):
        Driver.straight(10)
        Driver.turn(36)
        ev3.speaker.beep()
        Driver.straight(-20)

    Driver.straight(r.randint(1, 100))
    Driver.straight(r.randint(-1, -100))
    ev3.speaker.beep()
    Driver.turn(360)
    Driver.turn(-360)
    ev3.speaker.beep()
