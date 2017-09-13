import RPi.GPIO as GPIO
import time
import sys

redPin = 11
greenPin = 12

def blink(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)

def turnOff(pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.LOW)

def redOn():
	blink(redPin)

def greenOn():
	blink(greenPin)

def redOff():
	turnOff(redPin)

def greenOff():
	turnOff(greenPin)

def main():
	try:
		print("\nPress ^C (control-C) to exit the program.\n")
		while True:
			redOn()
			time.sleep(0.75)
			redOff()
			time.sleep(0.75)
			greenOn()
			time.sleep(0.75)
			greenOff()
			time.sleep(0.75)
	except KeyboardInterrupt:
		pass
	finally:
		GPIO.cleanup()

if __name__ == '__main__':
	main()
