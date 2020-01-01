#!/usr/bin/env python3

# sudo apt-get install python3-dev python3-pip python3-spidev python3-rpi.gpio
# sudo pip3 install mfrc522

# should set pin GPIO12/32 to high when we see something we like

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

pin_number = 32 # BCM GPIO 12 is physical pin 32

valid_bands =  [ 584197446646, 584185892850, 584186412169 ]

while True: 
    print("Waiting for a band to read")
    reader = SimpleMFRC522()
    try:
            GPIO.setup(pin_number, GPIO.OUT)
            GPIO.output(pin_number, GPIO.LOW)
            id, text = reader.read()
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(pin_number, GPIO.OUT)
            GPIO.output(pin_number, GPIO.LOW)
            print("Saw Band:", id)
            print(text)
            if id in valid_bands:
                print("Should ask ring to go immediately green!")
                GPIO.output(pin_number, GPIO.HIGH)
            else:
                GPIO.output(pin_number, GPIO.HIGH)
                time.sleep(0.2)
                GPIO.output(pin_number, GPIO.LOW)
                time.sleep(0.2)
                GPIO.output(pin_number, GPIO.HIGH)
                print("Should ask ring to go to pulsing blue")
            time.sleep(1)
            GPIO.output(pin_number, GPIO.LOW)

    finally:
        GPIO.cleanup()
