#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
touch = TouchSensor(Port.S1)
ultrasonic = UltrasonicSensor(Port.S3)
left = Motor(Port.C)
right = Motor(Port.B)

def ReadDistance():
    far = ultrasonic.distance()
    return far

# Write your program here.
ev3.speaker.beep()

seeking = True
while seeking:
    for i in range(72):
        left.run_time(360, 1000, True, then=Stop.COAST)
        right.run_time(-360, 1000, True, then=Stop.COAST)