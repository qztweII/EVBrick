#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from time import sleep


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
ultrasonic = UltrasonicSensor(Port.S3)
left = Motor(Port.C)
right = Motor(Port.B)

def ReadDistance():
    distance = ultrasonic.distance()
    return distance

def RunTimeDrive(motor1, motor2, speed, time):
    motor1.run_time(speed, time, wait=False, then=Stop.COAST)
    motor2.run_time(speed, time, wait=False, then=Stop.COAST)
# Write your program here.
ev3.speaker.beep()

while True:
    RunTimeDrive(left, right, 60, 10000)
    sleep(1)
    ev3.speaker.beep()
    if ReadDistance < 100:
        left.run_time(360, 1000, wait=True, then=Stop.COAST)