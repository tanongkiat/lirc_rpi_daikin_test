#!/usr/bin/python
#in. receive all
import RPi.GPIO as GPIO
import math
import os
from datetime import datetime
from time import sleep

#Change Raw to True for Printout RAW_CODES to parse in .conf
#after paste the RAW_CODES add one more line 450 to make it works.
#when CODE more than 20,000 > bugs!!!! have to split 2 lines
# for example to have 452 25500 ->
# 452     20000
# 10      5500

raw = True

INPUT_WIRE = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_WIRE, GPIO.IN)



while True:
	value = 1
	# Loop until we read a 0
	while value:
		value = GPIO.input(INPUT_WIRE)		
	# Grab the start time of the command
	startTime = datetime.now()

	# Used to buffer the command pulses
	command = []

	# The end of the "command" happens when we read more than
	# a certain number of 1s (1 is off for my IR receiver)
	numOnes = 0

	# Used to keep track of transitions from 1 to 0
	previousVal = 0
	count = 0
	while True:
		if value != previousVal:
			# The value has changed, so calculate the length of this run
			now = datetime.now()
			pulseLength = now - startTime
			startTime = now
			pulse =  pulseLength.microseconds
			command.append((count,previousVal, pulseLength.microseconds))
			count += 1

		if value:
			numOnes = numOnes + 1
		else:
			numOnes = 0

		# 10000 is arbitrary, adjust as necessary
		if numOnes > 10000:
			break

		previousVal = value
		value = GPIO.input(INPUT_WIRE)
	for (i,val,pulse) in command :
		print ("{} {} {}".format(i,val,pulse))

	if raw :
		print ("===== RAW =====")	

		newLine = False
		for (i,val,pulse) in command:
			if newLine  :
				print (pulse)
				newLine = False
			else: 
				print ("{}	".format(pulse)),	
				newLine = True
