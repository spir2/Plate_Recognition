import cv2
import easyocr
import matplotlib.pyplot as plt

class PlateDetector:
    def __init__(self, lang=['en'], gpu=True):
        self.reader = easyocr.Reader(lang, gpu=gpu)

    def detect_and_display_text_live(self, threshold=0.48):
        cap = cv2.VideoCapture(0)  # Utilisez la caméra par défaut

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Erreur : Impossible de lire le flux vidéo.")
                break

            text_ = self.reader.readtext(frame)
            for bbox, text, score in text_:
                if score > threshold:
                    top_left = (int(bbox[0][0]), int(bbox[0][1]))
                    bottom_right = (int(bbox[2][0]), int(bbox[2][1]))
                    print(f"{text} || {round(score,2)}")
                    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 5)
                    cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)

            cv2.imshow('Détection de texte en direct', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = PlateDetector()
    detector.detect_and_display_text_live()
