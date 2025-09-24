def ssr_set(arg,swt):
  import RPi.GPIO as GPIO
#  import time
#  import sys
#
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(int(arg), GPIO.OUT) 
#
  if swt=="1":
    GPIO.output(int(arg), 1) 
  else:
    GPIO.output(int(arg), 0) 
  return
