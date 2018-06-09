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

def getquiz():
    done = False
    while not(done):
        choice = input("Which quiz would you like (1=addition, 2=subtraction, 3=multiplication) ? ")
        if choice in ['1','2','3']:
            done = True
        else:
            print("select 1, 2 or 3")
    return choice

def getquestion(a,b,whichquiz):
    question = "What is " + str(a)
    if whichquiz == '1':
        question = question + " + "
    if whichquiz == '2':
        question = question  + ' - '
    if whichquiz == '3':
        question = question + ' x '
    question = question + str(b) + ' ? '
    return question

def checkresponse(a,b,response, whichquiz):
    if whichquiz == '1':
        correct =  (a+b == response)
    elif whichquiz =='2':
        correct = (a-b == response)
    elif whichquiz == '3':
        correct = (a*b == response)
    if correct:
        return correct_pin
    else:
        return incorrect_pin

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(correct_pin, GPIO.OUT)
    GPIO.setup(incorrect_pin, GPIO.OUT)

    whichquiz = getquiz()

    while True:
        clear_pins()

        a = random.randint(0,12)
        b = random.randint(0,12)
        question = getquestion(a,b,whichquiz)
        response = input(question)
        try:
            response = int(response)
        except:
            response = None

        pin = checkresponse(a,b,response,whichquiz)

        light_pin(pin)
        time.sleep(2)


if __name__ == '__main__':
    main()