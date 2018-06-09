import RPi.GPIO as GPIO
import time

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    
    while True:
        GPIO.output(18, GPIO.HIGH)
        print("LED on")
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        print("LED off")
        time.sleep(1)
        

if __name__ == '__main__':
    main()