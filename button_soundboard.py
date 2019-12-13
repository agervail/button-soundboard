#!/usr/bin/env python3

import json
import os
from time import sleep
from pygame import mixer
import RPi.GPIO as GPIO
import sys

sounds = []
current_sounds_bank = 0
special_button_1 = 3
special_button_2 = 37

gpios_order = [3, 10, 15, 21, 26, 33,
               5, 11, 16, 22, 29, 35,
               7, 12, 18, 23, 31, 36,
               8, 13, 19, 24, 32, 37]

def create_sounds_table(sounds_banks, gpios_order):
    sounds = []
    for sb in sounds_banks:
        file_names = os.listdir(os.path.join('sounds', sb))
        sounds_dict = {}
        for fn in file_names:
            pos = int(fn.split('_')[0])
            sounds_dict[gpios_order[pos - 1]] = os.path.join('sounds', sb, fn)
        sounds.append(sounds_dict)
    return sounds


def button_callback(channel):
    global current_sounds_bank
    global sounds_banks

    if (channel == special_button_1 and not GPIO.input(special_button_2)) or (channel == special_button_2 and not GPIO.input(special_button_1)):
        current_sounds_bank += 1
        current_sounds_bank %= len(sounds_banks)
    else:
        print(channel)
        if channel in sounds[current_sounds_bank]:
            mixer.music.load(sounds[current_sounds_bank][channel])
            mixer.music.play()

sounds_bank_path = 'sounds'
sounds_banks = os.listdir(sounds_bank_path)

sounds = create_sounds_table(sounds_banks, gpios_order)

mixer.init()

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for gpio in gpios_order:
    GPIO.setup(int(gpio), GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(int(gpio), GPIO.FALLING, callback=button_callback, bouncetime=500)


while(not sleep(5)):
    pass
GPIO.cleanup() # Clean up
