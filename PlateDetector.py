import cv2
import easyocr
import matplotlib.pyplot as plt
import Run_a_PATH_in_VSCODE

class PlateDetector:
    def __init__(self, lang=['en'], gpu=True):
        self.reader = easyocr.Reader(lang, gpu=True)
        
    def load_image(self, image_path):
        img = cv2.imread(image_path)
        if img is None:
            print(f"Erreur : l'image {image_path} n'a pas pu être chargée. Vérifiez le chemin de l'image.")
            return None
        return img

    def detect_and_display_text(self, img, threshold=0.1):
        text_ = self.reader.readtext(img)
        i = 0
        for bbox, text, score in text_:
            print(text_[i])
            if score > threshold:
                # Les coins de la boîte englobante
                top_left = (int(bbox[0][0]), int(bbox[0][1]))
                bottom_right = (int(bbox[2][0]), int(bbox[2][1]))

                # Dessiner le rectangle et le texte
                cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
                cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
            i+=1
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        plt.show()

if __name__ == "__main__":

    # Utilisation de la classe
    detector = PlateDetector()

    image_paths = [
        'test2.png',
        'plate_BG.png',
        'plate2.png',
        'plaque3.png',
        # Ajoutez d'autres chemins d'images ici
    ]

    for path in image_paths:
        print("Chemin de l'image : ", path)
        img = detector.load_image(path)
        if img is not None:
            detector.detect_and_display_text(img)
