#include <Servo.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "DisplayManager.h"

Servo myservo;
DisplayManager displayManager;
const int ledPin = 10; 

void setup() {
  myservo.attach(9);  // servomoteur sur la broche 9
  Serial.begin(9600); // Initialise 

  pinMode(ledPin, OUTPUT); //LED en tant que sortie
  digitalWrite(ledPin, HIGH);
  displayManager.initialiser(); // Initialise l'affichage
  displayManager.effacer();
  displayManager.afficher("by :\nspir FPV", 2);
  displayManager.Update_screen();
  delay(2000);
  displayManager.effacer();
  displayManager.Update_screen();
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    if (command == "OPEN") {
      myservo.write(90);
      digitalWrite(ledPin, LOW); // Allume la LED
      displayManager.effacer();
      displayManager.afficher("Open", 3);
      displayManager.Update_screen();
      delay(5000);
      displayManager.effacer();
      displayManager.afficher("Fermeture", 2);
      displayManager.Update_screen();
      myservo.write(0);
      digitalWrite(ledPin, HIGH); // Éteint la LED
    }
    else if (command == "CLOSE") {
      myservo.write(0);
      digitalWrite(ledPin, HIGH); // Éteint la LED
      displayManager.effacer();
      displayManager.afficher("Close", 3);
      displayManager.Update_screen();
    }
  }
}
