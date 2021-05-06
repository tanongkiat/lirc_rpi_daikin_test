#testoutput
import RPi.GPIO as GPIO
import math
import os
from datetime import datetime
from time import sleep


# This is for revision 1 of the Raspberry Pi, Model B
# This pin is also referred to as GPIO23 == WIRE 16 , WIRE 11 = GPIO 17
# 1. pulse 430  space 430   = bit '0'   
# 2. pulse 430  space 1320  = bit '1'
# 3. pulse 430  space 25000 = short separator (A)
# 4. pulse 3440 space 1720  = leading bit (B)
# 5. pulse 430  space 35500 = long separator (C)
# SHORT - 400 -500 
# MEDIUM = 1000 - 5000
# LONG = 20000 - 30000
# VERYLONG > 30000

SHORT = 460
MEDIUM = 1500
LONG = 25500
LONGEST = 30000
#microsecond

OUTPUT_WIRE = 15
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUTPUT_WIRE, GPIO.OUT)
raw = ""


GPIO.output(OUTPUT_WIRE,0)
while True:
	GPIO.output(OUTPUT_WIRE,1)
	sleep(1)
	GPIO.output(OUTPUT_WIRE,0)	
	sleep(1)

	
	