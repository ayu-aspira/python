import RPi.GPIO as gpio
from moto import *


class GpioServo:
    def __init__(self, gpioImpl, pinNum, frequency):
        self.gpioImpl = gpioImpl
        gpioImpl.setmode(gpioImpl.BOARD)
        gpioImpl.setup(pinNum, gpioImpl.OUT)
        self.servo = gpioImpl.PWM(pinNum, frequency)

    def start(self):
        self.servo.start(0)

    def setDutyCycle(self, duty):
        self.servo.ChangeDutyCycle(duty)

    def stop(self):
        self.servo.stop()
        self.gpioImpl.cleanup()


if __name__ == '__main__':
    runServo(Servo(GpioServo(gpio, 11, 50)))
