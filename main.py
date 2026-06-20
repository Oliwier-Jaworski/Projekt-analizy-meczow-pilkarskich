
import cv2
import numpy as np
from ultralytics import YOLO

def main():
    # Ścieżka do pliku z folderu data - potem ewentualnie z ekranu ze streama będę próbował
    sciezka = "data/DFL_Bundesliga_Data_Shootout/test/test (2).mp4"

    # Inicjalizacja obiektu do przechwytywania wideo
    cap = cv2.VideoCapture(sciezka)

    # Sprawdzenie czy wszystko działa z otwieraniem pliku
    if not cap.isOpened():
        print(f"Błąd w otwieraniu pliku wideo - nie można załadować z {sciezka}")
        return

    print("Udało się odtworzyć film. Wciśnij 'q' aby przerwać")

    # Inicjalizacja modelu YOLO do analizy
    # na ten moment wersja nano - potem wytestuję jeszcze wersję small
    model = YOLO("yolov8n.pt")
    #model = YOLO("yolov8s.pt")


    print("Rozpoczynam pętlę odczytu...")
    licznik_klatek = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print(f"Koniec strumienia. Łącznie odczytano klatek: {licznik_klatek}")
            break

        licznik_klatek += 1

        # PRZEWIDYWANIE
        # verbose false ukrywa spam w konsoli
        # klasa 0 ludzie, klasa 32 piłka sportowa
        results = model.predict(frame, classes=[0,32], verbose=False)


        # PRZETWARZANIE WYMIKÓW I RYSOWANIE
        # użyjemy funkcji wbudowanej w ultralytics
        # labels false wyłącza nazwy ramek, conf wyłącza false stopień pewności
        annotated_frame = results[0].plot(labels=False, conf=False)


        # Wyświetlenie klatki
        cv2.imshow("Analiza Wideo", annotated_frame)

        # Kluczowe opóźnienie: 30ms daje ~30 FPS. - do dostosowania w przyszłości
        if cv2.waitKey(20) & 0xFF == ord('q'):
            print(f"Przerwano ręcznie. Odczytano klatek: {licznik_klatek}")
            break

    # Sprzątanie pamięci
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()