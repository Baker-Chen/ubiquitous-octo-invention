import time
import RPi.GPIO as GPIO


class Sensor():
    def __init__(self):
        self.__TRIG = 19 
        self.__ECHO = 21 
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(self.__TRIG,GPIO.OUT)
        GPIO.setup(self.__ECHO,GPIO.IN)

    def getDistance(self):
        GPIO.output(self.__TRIG, GPIO.LOW)

        GPIO.output(self.__TRIG, True)

        time.sleep(0.00001)        
        GPIO.output(self.__TRIG, False)

        signaloff=0
        signalon=0
        
        while GPIO.input(self.__ECHO) == 0:
            signaloff = time.time()
        
        while GPIO.input(self.__ECHO) == 1:
            signalon = time.time()
        
        return (signalon - signaloff) * 17000

    def __del__(self):
        GPIO.cleanup()


def main():

    sensor = Sensor()

    while True:
        distance = sensor.getDistance()
        print("{:.0f}cm".format(distance))

        time.sleep(0.1)
    del sensor

if __name__ == '__main__':
    main()