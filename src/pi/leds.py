#!/usr/bin/env python
# leds.py

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7)
GPIO.setup(11)
GPIO.setup(12)
GPIO.output(7, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)
GPIO.output(12, GPIO.HIGH)

GPIO.cleanup()