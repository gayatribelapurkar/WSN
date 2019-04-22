#include <RF24.h>
#include <RF24Network.h>
#include <SPI.h>

int temppin=2;
float tempf, tempc;
RF24 radio(9, 10);               // nRF24L01 (CE,CSN)
RF24Network network(radio);      // Include the radio in the network
const uint16_t this_node = 00; 
const uint16_t node01 = 01;   
const uint16_t node02 = 02;   // Address of our node in Octal format ( 04,031, etc)
const uint16_t node03 = 03;
const uint16_t node04 = 04;

void setup() {
  SPI.begin();
  Serial.begin(57600);
  radio.begin();
  network.begin(90, this_node); //(channel, node address)
  

}
void loop() {
  network.update();
  while ( network.available() ) {     // Is there any incoming data?
    RF24NetworkHeader header;
    
    float incomingData;
    float node1_data;
    float node2_data;
    float node3_data;
    float node4_data;
    const char text[10];
    char text1[16];
    char sendVal[50];
    String str;
    network.read(header, &incomingData, sizeof(incomingData)); // Read the incoming data
   
    if (header.from_node == 01) {    // If data comes from Node 02
     // myservo.write(incomingData);  // tell servo to go to a particular angle
     node1_data= incomingData;
     Serial.println("the data from node 1 is ");
     Serial.println(node1_data);
     str="01_" + String(node1_data);
     Serial.println(str);
     int strl = str.length()+1;
     str.toCharArray(sendVal, strl);
     Serial.println(sendVal);
//     delay(1000);
    }
    
    if (header.from_node ==02) {    // If data comes from Node 012
      //digitalWrite(led, !incomingData);  // Turn on or off the LED 02
     node2_data= incomingData;
     Serial.println("the data from node 2 is");
     Serial.println(node2_data);

     str="02_" + String(node2_data);
     Serial.println(str);
     int strl = str.length()+1;
     str.toCharArray(sendVal, strl);
     Serial.println(sendVal);
//     delay(1600);
    }

     if (header.from_node == 03) {    // If data comes from Node 02
     // myservo.write(incomingData);  // tell servo to go to a particular angle
     node3_data= incomingData;
     Serial.println("the data from node 3 is ");
     Serial.println(node3_data);

     str="03_" + String(node3_data);
     Serial.println(str);
     int strl = str.length()+1;
     str.toCharArray(sendVal, strl);
     Serial.println(sendVal);
//     delay(2200);
    }

    if (header.from_node == 04) {    // If data comes from Node 02
     // myservo.write(incomingData);  // tell servo to go to a particular angle
     node4_data= incomingData;
     Serial.println("the data from node 4 is ");
     Serial.println(node4_data);

     str="04_" + String(node4_data);
     Serial.println(str);
     int strl = str.length()+1;
     str.toCharArray(sendVal, strl);
     Serial.println(sendVal);
//     delay(2800);
    }

     tempf=analogRead(temppin); // Reading data from the sensor.This voltage is stored as a 10bit number
     tempf=(5.0*tempf*1000.0)/(1024*10);
//  (32°F − 32) × 5/9 = 0°C
     tempc = (tempf-32)*5/9;
//  dtostrf(tempc, 6, 2, text);
     Serial.println("The value of the sensor in parent gateway is");
     Serial.println(tempc);

     str="05_" + String(tempc);
     Serial.println(str);
     int strl = str.length()+1;
     str.toCharArray(sendVal, strl);
     Serial.println(sendVal);
//     delay(4600);
    
  }
}
  
