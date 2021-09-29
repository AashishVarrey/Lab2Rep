import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led1 = 4
led2 = 13
led3 = 12
topbutton = 24
bottombutton = 25

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(topbutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bottombutton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

f = 1
dc = 50
pwm1 = GPIO.PWM(led1,f)
pwm2 = GPIO.PWM(led2,f)

def my_callback(channel):
    if channel == topbutton:
        pwm1.start(0)
        for x in range(101):
            pwm1.ChangeDutyCycle(x)
            sleep(0.01)
        for y in range(100,0,-1):
            pwm1.ChangeDutyCycle(y)
            sleep(0.01)
        print("top")
        pwm1.stop()
    if channel == bottombutton:
        pwm2.start(0)
        for x in range(101):
            pwm2.ChangeDutyCycle(x)
            sleep(0.01)
        for y in range(100,0,-1):
            pwm2.ChangeDutyCycle(y)
            sleep(0.01)
        print("bottom")
        pwm2.stop()


try:
    pwm = GPIO.PWM(led3,f)
    pwm.start(dc)
    GPIO.add_event_detect(topbutton, GPIO.RISING, callback=my_callback)
    GPIO.add_event_detect(bottombutton, GPIO.RISING, callback=my_callback)
    while True:
        pass
except KeyboardInterrupt:
    print('\nExiting')

pwm.stop()
GPIO.cleanup()

