import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

def ping ():
    "Hardware operations"
    GPIO.output(TRIG, False)
    # sonic burst
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    return pulse_end - pulse_start;

print "Distance measurement in progress"
# GPIO setup
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

print "Waiting for sensor to settle..."
time.sleep(1)

try:
    while True:
        pulse_duration = ping()
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print "Distance:",distance,"cm"
        time.sleep(0.5)
except KeyboardInterrupt:
    print "Exiting now!"
finally:
    # clean exit
    GPIO.cleanup()
