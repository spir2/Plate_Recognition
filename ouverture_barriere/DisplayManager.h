#ifndef DISPLAY_MANAGER_H
#define DISPLAY_MANAGER_H

#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

class DisplayManager {
public:
  void initialiser();
  void effacer();
  void afficher(const char* message, float text_size);
  void afficher(const char* message,float  text_size ,int x, int y);
  void Update_screen();
private:
  Adafruit_SSD1306 display;
};

void DisplayManager::initialiser() {
  Wire.begin(A4, A5); 
  
  display = Adafruit_SSD1306(128, 64, &Wire);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C); // Initialise l'écran OLED
  //display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
}

void DisplayManager::afficher(const char* message, float text_size, int x, int y) {
  display.setTextSize(text_size);
  //display.clearDisplay();
  display.setCursor(x,y);
  display.print(message);
  //display.display();
}

void DisplayManager::afficher(const char* message, float text_size) {
  afficher(message, text_size, 0, 0); 
}

void DisplayManager::effacer() {
  display.clearDisplay();
  //display.display(); 
}

void DisplayManager::Update_screen() {
  display.display();
}

#endif
