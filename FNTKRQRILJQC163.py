#This program is necessary for the 'on' button on my coffee maker,
#which has two buttons that both act as a toggle.

#You may need to edit this and doGPIO.py to make it work with your coffee maker

import RPi.GPIO as GPIO

#initializes GPIO pins and sets pin 7 to true (on)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.output(7,True)