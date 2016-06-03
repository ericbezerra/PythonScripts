import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,50)
p.start(7.5)

try:
    while True:
        GPIO.output(7,1)
        time.sleep(0.0015)
        GPIO.output(7,0)
        time.sleep(2)

exept KeyboardInterrupt:
    GPIO.cleanup()
