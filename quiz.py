import RPi.GPIO as GPIO
import time
import random

correct_pin = 14
incorrect_pin = 15

def clear_pins():
    GPIO.output(correct_pin, GPIO.LOW)
    GPIO.output(incorrect_pin, GPIO.LOW)

def light_pin(pin):
    GPIO.output(pin, GPIO.HIGH)

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(correct_pin, GPIO.OUT)
    GPIO.setup(incorrect_pin, GPIO.OUT)

    while True:
        clear_pins()

        a = random.randint(0,10)
        b = random.randint(0,10)
        question = "What is " + str(a) + " x " + str(b) + ' ? '
        answer = a * b
        response = input(question)
        try:
            response = int(response)
        except:
            response = None

        if response == answer:
            pin = correct_pin
            # print("Correct!")
        else:
            print("Incorrect")
            # pin = incorrect_pin

        light_pin(pin)
        time.sleep(3)


if __name__ == '__main__':
    main()