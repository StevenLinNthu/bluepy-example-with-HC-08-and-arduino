#include <SoftwareSerial.h>

SoftwareSerial BT(10, 9); 
String val; 
 
void setup() {
  Serial.begin(9600);  
  Serial.println("BT is ready!");
 
  BT.begin(9600);
}
 
void loop() {

  if (Serial.available()) {
    val = Serial.readString();
    Serial.print("Send: ");
    Serial.println(val);
    BT.print(val);
  }
 
  if (BT.available()) {
    val = BT.readString();
    Serial.print("Recieved: ");
    Serial.println(val);
  }
}
