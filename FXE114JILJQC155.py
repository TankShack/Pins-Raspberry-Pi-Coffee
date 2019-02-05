#RPi.GPIO is the library for the GPIO pins
import RPi.GPIO as GPIO

#time allows for delays with the 'sleep' function
import time

#initialize the GPIO pins on the RPi
GPIO.setmode(GPIO.BOARD)

#set the 7th pin (3.3V controllable) to output signal
GPIO.setup(7,GPIO.OUT)

#send a signal for one second, then stop
GPIO.output(7,True)
time.sleep(1)
GPIO.output(7,False)
time.sleep(1)
   
#resets the GPIO settings
GPIO.cleanup()