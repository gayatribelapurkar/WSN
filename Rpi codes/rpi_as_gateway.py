import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
from time import sleep
import spidev
from sendData import connection

GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.openReadingPipe(1, pipes[1])
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()
radio.printDetails()


def change_params2(radio):
    radio.stopListening()
    #radio.closeReadingPipe(0)
    #radio.openReadingPipe(1, pipes[0])
    radio.setChannel(0x52)
    radio.startListening()
    print("Node 2")
#    sleep(2)

def change_params3(radio):
    radio.stopListening()
    #radio.closeReadingPipe(0)
    #radio.openReadingPipe(1, pipes[0])
    radio.setChannel(0x53)
    radio.startListening()
    print("Node 3")
#    sleep(2)

def change_params4(radio):
    radio.stopListening()
    #radio.closeReadingPipe(0)
    #radio.openReadingPipe(1, pipes[0])
    radio.setChannel(0x54)
    radio.startListening()
    print("Node 4")
#    sleep(2)

def change_params5(radio):
    radio.stopListening()
    #radio.closeReadingPipe(0)
    #radio.openReadingPipe(1, pipes[0])
    radio.setChannel(0x55)
    radio.startListening()
    print("Node 2")
#    sleep(2)


def revert_params(radio):
    radio.stopListening()
    #radio.closeReadingPipe(1,pipes[0])
    #radio.openReadingPipe(1, pipes[1])
    radio.setChannel(0x51)
    radio.startListening()
    print("Node 1")
    #sleep(1)

def takeData(radio):
    while not radio.available(0):
        sleep(1/100)
#        print("waiting")
    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    print("Received: {}".format(receivedMessage))

    print("Translating the receivedMessage into unicode characters")
    string = ""
    for n in receivedMessage:
        # Decode into standard unicode set
        if (n >= 48 and n <= 57):
            string += chr(n)
        if (n == 46):
            string += '.'
    print("Current Temperature: {}".format(string))
    temp = float(string)
    print(type(temp))
    print(temp)
    return temp
    #sleep(20)


while(1):
# ackPL = [1]
    revert_params(radio)
    sleep(1)
    temp1 = takeData(radio)
    
    change_params2(radio)
    sleep(1)
    temp2 = takeData(radio)
    
    change_params3(radio)
    sleep(1)
    temp3 = takeData(radio)
    
    change_params4(radio)
    sleep(1)
    temp4 = takeData(radio)
    
    change_params5(radio)
    sleep(1)
    temp5 = takeData(radio)
    
    connection(temp1,temp2,temp3,temp4,temp5)
    