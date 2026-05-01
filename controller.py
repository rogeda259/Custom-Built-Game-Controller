import RPi.GPIO as GPIO
import spidev
from time import sleep

# SPI setup
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

# GPIO setup
GPIO.setmode(GPIO.BCM)

buttonP = 17
buttonB = 27
buttonG = 22

GPIO.setup(buttonP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonG, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def readChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while(1):
        xpos = readChannel(6)
        ypos = readChannel(7)
        print("X-pos : {} Y-pos : {}".format(xpos, ypos))
        if GPIO.input(buttonP) == 0:
            print("Purple Button Pressed")
        if GPIO.input(buttonB) == 0:
            print("Blue Button Pressed")
        if GPIO.input(buttonG) == 0:
            print("Green Button Pressed")
        sleep(.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    spi.close()
