#!/usr/bin/python3
#
import RPi.GPIO as GPIO
import time
import sys
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)  # bottom heater
#
on=1;off=0
#
while True:
  try:
#
    GPIO.output(int(sys.argv[1]), 1) # 250331
    time.sleep(1)
#
    GPIO.output(int(sys.argv[1]), 0) # 250331
    time.sleep(1)
  except KeyboardInterrupt:
    GPIO.output(int(sys.argv[1]), 0) # 250331
    exit()
