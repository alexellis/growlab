
#include "Arduino_SensorKit.h"

#define LED 6
 
void setup() {
  // put your setup code here, to run once:
  pinMode(LED,OUTPUT);    //Sets the pinMode to Output 

  Serial.begin(9600);
  Environment.begin();
  //oled display does not work if air pressure (I²C) is used
  //Pressure.begin();

  Oled.begin();
  Oled.setFlipMode(true); // Sets the rotation of the screen
}
 
void loop() {
  // put your main code here, to run repeatedly:
 /*
  digitalWrite(LED, HIGH); //Sets the voltage to high 
  delay(1000);             //Waits for 1000 milliseconds 
  digitalWrite(LED, LOW);  //Sets the voltage to low
*/

  float temperatur = Environment.readTemperature();
  float humidity = Environment.readHumidity();
  float pressure = 1007;
  Serial.print("{ \"temperature\": \"");
  Serial.print(temperatur);
  Serial.print("\", ");
  Serial.print(" \"humidity\": \"");
  Serial.print(humidity);
   Serial.print("\", ");
  Serial.print(" \"pressure\": \"NoN");
  Serial.print(pressure);
  Serial.print("\" ");
  Serial.println(" }");;
 
  Oled.setFont(u8x8_font_chroma48medium8_r); 
  Oled.setCursor(0, 33);    // Set the Coordinates 
  Oled.print("temp °C:");
  Oled.print(temperatur); // Print the Values
  Oled.setCursor(0, 43);    // Set the Coordinates
  Oled.print("Humid: %:");   
  Oled.print(humidity); // Print the Values
  Oled.setCursor(0, 53);    // Set the Coordinates
  Oled.print("Pressure:");   
  Oled.print(pressure); // Print the Values
  Oled.refreshDisplay();    // Update the Display
  
  delay(3000);

}
