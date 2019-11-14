#!/usr/bin/env python3

import json
from pygame import mixer
import RPi.GPIO as GPIO
import sys

sounds = []
current_sounds_bank = 0
special_button_1 = 3
special_button_2 = 37

def button_callback(channel):
	global current_sounds_bank

	if (channel == special_button_1 and not GPIO.input(special_button_2)) or (channel == special_button_2 and not GPIO.input(special_button_1)):
		current_sounds_bank += 1
		current_sounds_bank %= len(sys.argv) - 1
	else:
		print(channel)
		mixer.music.load(sounds[current_sounds_bank][str(channel)])
		mixer.music.play()

if len(sys.argv) >= 2:
	for sounds_bank in range(len(sys.argv) - 1):
		with open(sys.argv[sounds_bank + 1], 'r') as f:
			sounds.append(json.load(f))

	mixer.init()

	GPIO.setwarnings(False) # Ignore warning for now
	GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

	used_gpios = []
	for sounds_bank in sounds:
		for gpio in sounds_bank:
			if int(gpio) not in used_gpios:
				GPIO.setup(int(gpio), GPIO.IN, GPIO.PUD_UP)
				GPIO.add_event_detect(int(gpio), GPIO.FALLING, callback=button_callback, bouncetime=500)
				used_gpios.append(int(gpio))

	message = input("Press enter to quit\n\n") # Run until someone presses enter

	GPIO.cleanup() # Clean up
