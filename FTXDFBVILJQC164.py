#several libraries are imported

#os lets us search a directory for files with a specific extension
#(in this case, we're looking for files ending with '.coffee')
import os

#time allows us to delay the loop at the end with the "sleep" command
import time

#call gives us the "call" commands, which talk to the RPi through the console
from subprocess import call

#call the GPIO initialization program  as the super user
#(you're not allowed to call coffeeBot.py as sudo)
call(["sudo", "python", "turnOnGPIO.py"])

#start the loop that comprises the repeated checking process
while 1:

	#initializes the mail string
    mail = ''

	#executes 'fetchmail' from console, which checks for new mail
    call(["fetchmail"])

	#searches the directory for files ending with '.coffee'
    fastq = [f for f in os.listdir('.') if f.endswith('.coffee')]

	#if array 'fastq' isn't empty, set 'mail' equal to filename
    if fastq:
        mail = fastq[0]

	#if mail isn't blank, call the program to send the signal to the coffee maker
    if mail:
        call(["sudo", "python", "doGpio.py"])
        print "\n---------------------------\nCOFFEE REQUEST RECEIVED!\n---------------------------\n"
        call(["rm", mail])
	
	#pause the program for three seconds
    time.sleep(3)
