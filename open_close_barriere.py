import cv2
import easyocr
import matplotlib.pyplot as plt
import re
import time
import serial

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
                break

            text_ = self.reader.readtext(frame)
            for bbox, text, score in text_:
                print("->",text)
                #self.plate = self.clean_plate(text)
                self.plate = text
                if score > threshold and self.plate:
                    print(f"-------->{self.plate}<--------")
                    top_left = (int(bbox[0][0]), int(bbox[0][1]))
                    bottom_right = (int(bbox[2][0]), int(bbox[2][1]))
                    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 5)
                    cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
                    var = False

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
    def __init__(self, serial_port):
        self.serial_port = serial.Serial(serial_port, 9600)  

    def open_barriere(self):
        print("Open")
        self.serial_port.write(b'OPEN\n')


    def close_barriere(self):
        print("Close")
        self.serial_port.write(b'CLOSE\n')

    def verif_barriere(self, verif):
        print(verif)
        L = ["AB123CD",
             "AD456KI",
             "AA000AA",
             "AA123AA",
             "AB344CA",
             "AA112AA",
             "AA725AD",
             "B2228HM"]
        if verif in L:
            return True
        return False


if __name__ == "__main__":
    detector = PlateDetector()
    barriere = Barriere('COM4') 
    boo = True
    while boo:
        detector.detect_and_display_text_live()
        if barriere.verif_barriere(detector.plate):
            barriere.open_barriere()
        else:
            barriere.close_barriere()

        #time.sleep(2)
