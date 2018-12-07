#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import cv2

try:
	GPIO.setmode(GPIO.BOARD)

	PIN_TRIGGER1 = 7
	PIN_ECHO1 = 11
	GPIO.setup(PIN_TRIGGER1, GPIO.OUT)
	GPIO.setup(PIN_ECHO1, GPIO.IN)
	PIN_TRIGGER2 = 13
	PIN_ECHO2 = 15
	GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
	GPIO.setup(PIN_ECHO2, GPIO.IN)
	while True:
		GPIO.output(PIN_TRIGGER1, GPIO.LOW)
		GPIO.output(PIN_TRIGGER2, GPIO.LOW)
		print "Waiting for sensor to settle"

		time.sleep(1)

		print "Calculating distance"

		GPIO.output(PIN_TRIGGER1, GPIO.HIGH)
		GPIO.output(PIN_TRIGGER2, GPIO.HIGH)
		time.sleep(0.00001)
 
		GPIO.output(PIN_TRIGGER1, GPIO.LOW)
		while GPIO.input(PIN_ECHO1)==0 and GPIO.input(PIN_ECHO2) ==0:
			pulse_start_time1 = time.time()
			pulse_start_time2 = time.time()
		while GPIO.input(PIN_ECHO1) ==1 and GPIO.input(PIN_ECHO2) ==0:
			pulse_end_time1 = time.time()
			pulse_end_time2 = time.time()

		pulse_duration1 = pulse_end_time1 - pulse_start_time1
		distance1 = round(pulse_duration1 * 17150, 2)
		print "Distance1:", distance1,"cm"
		pulse_duration2 = pulse_end_time2 - pulse_start_time2
		distance2 = round(pulse_duration2 *17150, 2)
		print "Distance2:", distance2,"cm"

except KeyboardInterrupt:
	print('interuptted!')

finally:
	GPIO.cleanup()
	print('cleaned')
