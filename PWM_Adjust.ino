#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

char input = ""; //serial input is stored in this variable
int Fan = 3;
int Speed = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  lcd.begin();  
  lcd.backlight();
  pinMode(Fan, OUTPUT);
  lcd.setCursor(0, 0);
  lcd.print("---PWM Adjust---");
  lcd.setCursor(0, 1);
  lcd.print("Speed: ");
  
}

void loop() {
  // put your main code here, to run repeatedly:
   if(Serial.available()){ //checks if any data is in the serial buffer
      input = Serial.read(); //reads the data into a variable
          if(input == 'L'){
           Speed = 100;
           lcd.setCursor(7, 1);
           lcd.print("Slow");
           lcd.print("   ");
          }
          else if(input == 'M'){ 
           Speed = 200;
           lcd.setCursor(7, 1);
           lcd.print("Medium");
           lcd.print("   ");
          }
          else if(input == 'H'){ 
           Speed = 255;
           lcd.setCursor(7, 1);
           lcd.print("Fast");
           lcd.print("   ");
          }
          else{
           Speed = 0;
           lcd.setCursor(7, 1);
           lcd.print("OFF");
           lcd.print("   ");
          } 
       analogWrite(Fan, Speed);
  }
}
