import RPi.GPIO as gpio
from time import sleep

ledPin = (16, 21)

gpio.setmode(gpio.BCM)
for pin in ledPin:
    gpio.setup(pin, gpio.OUT)

currentPassword = None

while True:
    newPassword = input("new password: ")
    confirmPassword = input("confirm password: ")
    if newPassword == confirmPassword:
        currentPassword = newPassword
        print("비번이 설정됨")
        break
    else:
        print("비번이 잘못입력됨")

while True:
    login password = ("login password: ")
    if loginpassword == currentPassword:
        gpio.output(ledPin[1], gpio.HIGH)
        break
    else:
        for i in range(5):
            gpio.output(pin[0], gpio.HIGH)
            sleep(0.1)
            gpio.output(pin[0], gpio.LOW)
            sleep(0.1)
        