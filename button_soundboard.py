#!/usr/bin/env python3

import json
from pygame import mixer
import RPi.GPIO as GPIO
import sys

def button_callback(channel):
	print(channel)
	mixer.music.load(sounds[str(channel)])
	mixer.music.play()

if len(sys.argv) == 2:
	with open(sys.argv[1], 'r') as f:
		sounds = json.load(f)

	mixer.init()

	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

	for gpio in sounds:
		GPIO.setup(int(gpio), GPIO.IN, GPIO.PUD_UP)
		GPIO.add_event_detect(int(gpio), GPIO.FALLING, callback=button_callback, bouncetime=500)

	message = input("Press enter to quit\n\n") # Run until someone presses enter

	GPIO.cleanup() # Clean up
