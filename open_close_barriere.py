import cv2
import easyocr
import matplotlib.pyplot as plt
import re

class PlateDetector:
    def __init__(self, lang=['en'], gpu=True):
        self.reader = easyocr.Reader(lang, gpu=gpu)
        self.plate = str()

    def detect_and_display_text_live(self, threshold=0.20):
        cap = cv2.VideoCapture(0)  

        var = True
        while var:
            ret, frame = cap.read()
            if not ret:
                print("Erreur : Impossible de lire le flux vidéo.")
                break

            text_ = self.reader.readtext(frame)
            for bbox, text, score in text_:
                print(text)
                self.plate = self.clean_plate(text)
                if score > threshold and self.plate:
                    print(f"--------> {self.plate} <--------")
                    top_left = (int(bbox[0][0]), int(bbox[0][1]))
                    bottom_right = (int(bbox[2][0]), int(bbox[2][1]))
                    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 5)
                    cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
                    var=False
            

            cv2.imshow('Détection de texte en direct', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def clean_plate(self, text):
        cleaned_text = ''.join(filter(str.isalnum, text))
        if re.match(r'^[A-Z]{2}\d{3}[A-Z]{2}$', cleaned_text, re.IGNORECASE):
            return cleaned_text
        else:
            return None

class Barriere:
    def __init__(self):
        pass

    def open_barriere():
        print("Open")
        #mettre la fonction pour ouvrir la barriere 
        

    def close_barriere():
        #mettre la fonction pour fermer la barriere 
        print("Close")

    def verif_barriere(verif):
        L=["AB123CD","AD456KI","AA000AA","AA123AA"]
        if verif in L: 
            return True
        return False
        
#Mettre programme de detection de plaque qui renverra la valeur de la plaque en parametre de la fct verif_barriere()

if __name__ == "__main__":
    detector = PlateDetector()
    barriere = Barriere()
    detector.detect_and_display_text_live()
print("test",detector.plate)
if Barriere.verif_barriere(detector.plate):

    Barriere.open_barriere()
else :
    Barriere.close_barriere()
