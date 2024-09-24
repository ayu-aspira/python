from time import sleep
from threading import Thread


class ServoImplTest:
    def start(self):
        print('started')

    def setDutyCycle(self, duty):
        print('current duty: ' + str(duty))

    def stop(self):
        print('stopped')


class Servo:

    MANUAL = 0
    AUTO = 1

    DUTY_FOR_0 = 2
    DUTY_FOR_180 = 12
    DUTY_ONE_STEP_DEGREE = 18

    def __init__(self, servoImpl):
        self.runFlag = True
        self.servoImpl = servoImpl
        self.currentModel = Servo.MANUAL

    def start(self):
        self.servoImpl.start()
        sleep(1)
        duty = Servo.DUTY_FOR_0
        while (self.runFlag):
            if (self.currentModel == Servo.MANUAL):
                sleep(0.1)
            elif (self.currentModel == Servo.AUTO):
                duty = Servo.DUTY_FOR_0 if duty > Servo.DUTY_FOR_180 else duty
                self.__changeDuty(duty)
                duty = duty + 1

    def setModel(self, model):
        self.currentModel = model

    def changeDuty(self, duty):
        if (self.currentModel == Servo.AUTO):
            print('change model to manual first.')
            return
        print('change duty to  :' + str(duty))
        self.__changeDuty(duty)

    def stop(self):
        self.runFlag = False
        self.servoImpl.stop()

    def __changeDuty(self, duty):
        if duty < Servo.DUTY_FOR_0 or duty > Servo.DUTY_FOR_180:
            return
        self.servoImpl.setDutyCycle(duty)
        sleep(0.2)
        self.servoImpl.setDutyCycle(0)
        sleep(0.3)


def runServo(servo):
    thread = Thread(target=servo.start)
    thread.start()
    runFlag = True
    while runFlag:
        value = input("Enter Angle(0 to 180)/stop/manual/auto: ")
        if (value == 'stop'):
            runFlag = False
            servo.stop()
        elif (value.isnumeric()):
            tempDuty = (Servo.DUTY_FOR_0 +
                        (int(value)/Servo.DUTY_ONE_STEP_DEGREE))
            print('caluculated duty near : ' + str(round(tempDuty)))
            servo.changeDuty(round(tempDuty))
        elif (value == 'manual'):
            servo.setModel(Servo.MANUAL)
        elif (value == 'auto'):
            servo.setModel(Servo.AUTO)
        else:
            print('UnKnown Command')
        sleep(0.1)


if __name__ == '__main__':
    runServo(Servo(ServoImplTest()))
