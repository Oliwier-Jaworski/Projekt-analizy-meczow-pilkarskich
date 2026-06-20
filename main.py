
import cv2
import numpy as np

def main():
    # Ścieżka do pliku z folderu data - potem ewentualnie z ekranu ze streama będę próbował
    sciezka = "data/DFL_Bundesliga_Data_Shootout/test/test (1).mp4"

    # Inicjalizacja obiektu do przechwytywania wideo
    cap = cv2.VideoCapture(sciezka)

    # Sprawdzenie czy wszystko działa z otwieraniem pliku
    if not cap.isOpened():
        print(f"Błąd w otwieraniu pliku wideo - nie można załadować z {sciezka}")
        return

    print("Udało się odtworzyć film. Wciśnij 'q' aby przerwać")

    print("Rozpoczynam pętlę odczytu...")
    licznik_klatek = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print(f"Koniec strumienia. Łącznie odczytano klatek: {licznik_klatek}")
            break

        licznik_klatek += 1

        # Wyświetlenie klatki
        cv2.imshow("Analiza Wideo", frame)

        # Kluczowe opóźnienie: 30ms daje ~30 FPS. - do dostosowania w przyszłości
        if cv2.waitKey(30) & 0xFF == ord('q'):
            print(f"Przerwano ręcznie. Odczytano klatek: {licznik_klatek}")
            break

    # Sprzątanie pamięci
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()