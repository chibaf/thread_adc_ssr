import time
import ADS1256
import RPi.GPIO as GPIO
import ssr_set

#GPIO.setup(35, GPIO.OUT)  # bottom heater


try:
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    while(1):
        ADC_Value = ADC.ADS1256_GetAll()
        print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
        print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
        print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
        print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
        print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
        print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
        print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
        print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))
        print ("\33[9A")
        #ADC.ADS1256_init()
        #ssr_set.ssr_set(35,1)

except :
    GPIO.cleanup()
    print ("\r\nProgram end     ")
    exit()
