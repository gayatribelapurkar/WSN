import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev
from urllib.request import urlopen

APIkey = "KKBT2QQLBR4AAOLP"
baseURL = "https://api.thingspeak.com/update?api_key=KKBT2QQLBR4AAOLP&field1=0"

GPIO.setmode(GPIO.BCM)

pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

radio = NRF24(GPIO, spidev.SpiDev())
radio.begin(0, 17)

radio.setPayloadSize(32)
radio.setChannel(0x60)
radio.setDataRate(NRF24.BR_1MBPS)
radio.setPALevel(NRF24.PA_MIN)

radio.setAutoAck(True)
radio.enableDynamicPayloads()
radio.enableAckPayload()

radio.openWritingPipe(pipes[0])
radio.openReadingPipe(1, pipes[1])
radio.printDetails()
# radio.startListening()
while(1):
    start = time.time()
    radio.startListening()

    while not radio.available(0):
        #print("Radio Not Available")
        time.sleep(1 / 100)

    receivedMessage = []
    radio.read(receivedMessage, radio.getDynamicPayloadSize())
    print("Received: {}".format(receivedMessage))

    #print("Translating the receivedMessage into unicode characters")
    string = ""
#    cel = "°C"
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
    
    try:
        #conn = urlopen((baseURL + '&field0={}').format(float(string)))
        conn = urlopen((baseURL + '&field1=%f') % (temp))
        print(conn.read())
            # Closing the connection
        conn.close()
    except Exception as e:
        print('Error')
        print(e)
        
    radio.stopListening()
    time.sleep(15)
    