
import cv2
import numpy as np

def main():
    # Ścieżka do pliku z folderu data - potem ewentualnie z ekranu ze streama będę próbował
    sciezka = "data/         .mp4"

    # Inicjalizacja obiektu do przechwytywania wideo
    cap = cv2.VideoCapture(sciezka)

    # Sprawdzenie czy wszystko działa z otwieraniem pliku
    if not cap.isOpened():
        print(f"Błąd w otwieraniu pliku wideo - nie można załadować z {sciezka}")
        return

    print("Udało się odtworzyć film. Wciśnij 'q' aby przerwać")

    while True:

        ret, frame = cap.read() # ret (bool) mówi czy została pobrana klatka, frame to nasza klatka (macierz pikseli)

        if not ret:
            print("Koniec strumienia wideo")
            break

        # TU BEDZIE LOGIKA PROGRAMU
        #
        #
        #
        #
        #
        #


        # Wyświetlenie przetworzonej klatki na ekranie
        cv2.imshow("Frame", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):  # czekamy 0,25s na reakcję klawiatury, warunek 0xFF upewnia się że q zostanie dobrze odczytane z bitów (sprawdza tylko ostatnie 8)
            print("Zamykanie programu")
            break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()