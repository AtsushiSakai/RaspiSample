import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

while True:
    print("High")
    GPIO.output(25, GPIO.HIGH)
    sleep(0.5)
    print("Low")
    GPIO.output(25, GPIO.LOW)
    sleep(0.5)
