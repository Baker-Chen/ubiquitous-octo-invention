from UART import uart
from ultraSonic import Sensor
from gestureElevator import gestureRecogFloor

################################################
# Collecting data from ultraSonicSensor and uart
# if receive a trigger signal then start 
# hand pose recognize module.
################################################

print("############START#############")

sensor = Sensor()

trigger = False
uart_trig = "N"
while True:
    distance = sensor.getDistance()

    if trigger == False:
        try:
            uart_trig, trigger = uart(COM_PORT = "/dev/ttyUSB0",BAUD_RATES = 115200)
        except:
            print("COM port error !")

    else:
        if distance <= 15 and distance > 0:
            print("Ultra Sonic trig, distance = %f" %distance)
            print("=======Triggered state========")
            print("  ---gestureRecog start---  ")
            trigger = gestureRecogFloor()
            print("  ----gestureRecog end----  ")

        elif distance > 15 :
            print("==========IDLE state==========")

            if uart_trig == "-1":
                print("KeyboardInterrupt !")
            else:
                if uart_trig == "Y":
                    print("Himax WE-I trig, Hand detect = %s cm" %uart_trig)
                    print("=======Triggered state========")
                    print("  ---gestureRecog start---  ")
                    trigger = gestureRecogFloor()
                    print("  ----gestureRecog end----  ")

                else:
                    print("==========IDLE state==========")
                    trigger = False
        