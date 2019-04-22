//Send.ino

#include<SPI.h>
#include<RF24.h>

int temppin=2;
float tempf, tempc;

// ce, csn pins
RF24 radio(9, 10);

void setup(void){
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x60);
  radio.openWritingPipe(0xF0F0F0F0E1LL);
  radio.enableDynamicPayloads();
  radio.powerUp();

}

void loop(void){
//  const char text[] = "Hello World is awesome --Gayatri";
  const char text[10];
  tempf=analogRead(temppin); // Reading data from the sensor.This voltage is stored as a 10bit number
  tempf=(5.0*tempf*1000.0)/(1024*10);
//  (32°F − 32) × 5/9 = 0°C
  tempc = (tempf-32)*5/9;
  dtostrf(tempc, 6, 2, text);
  radio.write(&text, sizeof(text));
  Serial.print(text);

  delay(1000);

}
