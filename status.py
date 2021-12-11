#! /usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

print(GPIO.input(25))

while True:
	print(GPIO.input(25), time.asctime())
	time.sleep(0.100)
