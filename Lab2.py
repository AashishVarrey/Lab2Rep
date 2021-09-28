import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

led1 = 21
led2 = 26
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

def my_callback(channel):
#  pwm23 = GPIO.PWM(channel,f)
#  pwm23.start(1)
  if channel == topbutton:
    pwm1 = GPIO.PWM(led1,1)
    for x in range(101):
      pwm1.ChangeDutyCycle(x)
    for y in range(101,0,-1):
      pwm1.ChangeDutyCycle(y)
    pwm.stop()  
    print("top")
  if channel == bottombutton:
    print("bottom")
#  if GPIO.input(channel) == GPIO.HIGH:
#  for x in range(101):
#    pwm.ChangeDutyCycle(x)
#  for y in range(101,0,-1):
#    pwm.ChangeDutyCycle(y)
#  pwm.stop()
#  else:
#    pass

pwm = GPIO.PWM(led3,f)

try:
    GPIO.add_event_detect(topbutton, GPIO.RISING, callback=my_callback)
    GPIO.add_event_detect(bottombutton, GPIO.RISING, callback=my_callback)
    pwm.start(dc)
    while True:
        pass
except KeyboardInterrupt:
    print('\nExiting')

pwm.stop()
GPIO.cleanup()

