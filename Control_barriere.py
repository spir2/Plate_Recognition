from easygopigo3 import EasyGoPiGo3
import time

# Initialisation
egpg = EasyGoPiGo3()
servo = egpg.init_servo()

def ouvrir_barriere():
    servo.rotate_servo(90)
    egpg.set_eye_color((0, 255, 0))  # Vert
    egpg.open_left_eye()
    egpg.open_right_eye()

def fermer_barriere():
    servo.rotate_servo(5)
    egpg.set_eye_color((255, 0, 0))  # Rouge
    egpg.open_left_eye()
    egpg.open_right_eye()

def etat_idle():
    servo.rotate_servo(5)
    for i in range(2):
        egpg.set_eye_color((255, 165, 0))  # Orange
        egpg.close_left_eye()
        egpg.open_right_eye()
        time.sleep(1)
        egpg.close_right_eye()
        egpg.open_left_eye()
        time.sleep(1)

while True:
    y = int(input("--> "))
    if y==1:
        ouvrir_barriere()
        print("open")
    elif y==2:
        fermer_barriere()
        print("fermer")
    else:
        etat_idle()
        fermer_barriere()
    time.sleep(0.1)


