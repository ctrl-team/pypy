#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
String data;
String firstRow = "";
String secondRow = "";
int count = 0;

void setup() {
  lcd.begin(16, 2);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available())
  {   
      data = char(Serial.read());

      if(count<16){
        firstRow+=data;
      }
      else if(count>=16 && count<32){
        secondRow+=data;
      }
      count++;

      /*
      if(count<16){
        firstRow+=data;
        count++;
      }
      else if(count>=16 && count<32){
        secondRow+=data;
        count++;
      }
      
      if(count>=32){
        count = -1;
        firstRow="";
        secondRow="";
      }
      */
  }
    lcd.setCursor(0,0);
    lcd.print(firstRow);

    lcd.setCursor(0,1);
    lcd.print(secondRow);
    delay(2000);
}
