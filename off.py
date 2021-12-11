#! /usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

GPIO.output(18,False)

while True:
	time.sleep(0.100)
	if GPIO.input(25):
		time.sleep(0.100)
		GPIO.output(18,False)
		break
	else:
		GPIO.output(18,False)
