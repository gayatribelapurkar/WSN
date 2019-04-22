#include <RF24.h>
#include <RF24Network.h>
#include <SPI.h>

int temppin=2;
float tempf, tempc;


RF24 radio(9,10);               // nRF24L01 (CE,CSN)
RF24Network network(radio);      // Include the radio in the network
const uint16_t this_node = 03;   // Address of this node in Octal format ( 04,031, etc)
const uint16_t node00 = 00; 

void setup() {
  SPI.begin();
  Serial.begin(57600);
  radio.begin();
  network.begin(90, this_node);  //(channel, node address)
  //Serial.begin(9600);                               //UART setup, baudrate = 9600bps
}
void loop() {
  
  network.update();
  
  tempf=analogRead(temppin); // Reading data from the sensor.This voltage is stored as a 10bit number
  tempf=(5.0*tempf*1000.0)/(1024*10);
//  (32°F − 32) × 5/9 = 0°C
  tempc = (tempf-32)*5/9;
//  dtostrf(tempc, 6, 2, text);
  
  Serial.println("The value of the sensor is");
  Serial.println(tempc);
  RF24NetworkHeader header(node00);     // (Address where the data is going)
  bool ok = network.write(header, &tempc, sizeof(tempc));
  delay(2000);
  
}


