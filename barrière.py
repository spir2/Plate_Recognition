from gpiozero import Servo
from time import sleep
#------------------------------Variables----------------------------------

open_close = True

#-------------------------------------------------------------------------
#------------------------------Functions----------------------------------
#-------------------------------------------------------------------------

def ouvrir_barriere():
    servo.value = 0  #Mid-point
    print("Open")

def fermer_barriere():
    servo.value = -1  #Minimum position
    print("Close")

#-------------------------------------------------------------------------
#------------------------------Programme----------------------------------
#-------------------------------------------------------------------------*

SERVO_PIN = 18  

# Initialisation du servo moteur
servo = Servo(SERVO_PIN)

if open_close == True :
    ouvrir_barriere()
else :
    fermer_barriere()




