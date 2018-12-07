#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import cv2

try:
	GPIO.setmode(GPIO.BOARD)

	PIN_TRIGGER1 = 7
	PIN_ECHO1 = 11
	PIN_TRIGGER2 = 13
	PIN_ECHO2 = 15
	PIN_TRIGGER3 = 16
	PIN_ECHO3 = 18
	GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
	GPIO.setup(PIN_ECHO1, GPIO.IN)
	GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
	GPIO.setup(PIN_ECHO2, GPIO.IN)
	GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
	GPIO.setup(PIN_ECHO3, GPIO.IN)
	while True:
		GPIO.output(PIN_TRIGGER1, GPIO.LOW)

		print "Waiting for sensor to settle"

		time.sleep(0.5)

		print "Calculating distance"

		GPIO.output(PIN_TRIGGER1, GPIO.HIGH)

		time.sleep(0.00001)

		GPIO.output(PIN_TRIGGER1, GPIO.LOW)
		while GPIO.input(PIN_ECHO1)==0:
			 pulse_start_time = time.time()
		while GPIO.input(PIN_ECHO1) ==1:
			pulse_end_time = time.time()

		pulse_duration = pulse_end_time - pulse_start_time
		distance = round(pulse_duration * 17150, 2)
		print "Distance1:", distance,"cm"





		GPIO.output(PIN_TRIGGER2, GPIO.LOW)
		time.sleep(0.5)

		GPIO.output(PIN_TRIGGER2, GPIO.HIGH)

		time.sleep(0.00001)

		GPIO.output(PIN_TRIGGER2, GPIO.LOW)
		while GPIO.input(PIN_ECHO2)==0:
			 pulse_start_time2 = time.time()
		while GPIO.input(PIN_ECHO2) ==1:
			pulse_end_time2 = time.time()

		pulse_duration = pulse_end_time2 - pulse_start_time2
		distance = round(pulse_duration * 17150, 2)
		print "Distance2:", distance,"cm"
		
		
		
		GPIO.output(PIN_TRIGGER3, GPIO.LOW)
		time.sleep(0.5)

		GPIO.output(PIN_TRIGGER3, GPIO.HIGH)

		time.sleep(0.00001)

		GPIO.output(PIN_TRIGGER3, GPIO.LOW)
		while GPIO.input(PIN_ECHO3)==0:
			 pulse_start_time3 = time.time()
		while GPIO.input(PIN_ECHO3) ==1:
			pulse_end_time3 = time.time()

		pulse_duration = pulse_end_time3 - pulse_start_time3
		distance = round(pulse_duration * 17150, 2)
		print "Distance3:", distance,"cm\n"

except KeyboardInterrupt:
	print('interuptted!')

finally:
	GPIO.cleanup()
	print('cleaned')
