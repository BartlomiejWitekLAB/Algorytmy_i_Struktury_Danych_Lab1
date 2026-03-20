import random


def gra_w_zgadywanie():
    print("--- Gra w zgadywanie liczby ---")

    # 1.1 Wybierz losowo liczbę z zakresu od 1 do 100
    wylosowana_liczba = random.randint(1, 100)

    # 1.2 Ustaw licznik prób na 1
    licznik_prob = 1

    print("Wylosowałem liczbę z zakresu od 1 do 100. Spróbuj ją odgadnąć!")

    # Nieskończona pętla, z której wyjdziemy instrukcją 'break'
    while True:
        try:
            # 1.3 Poproś użytkownika o wpisanie liczby
            podana_liczba = int(input("\nWpisz swoją liczbę: "))

            # 1.3.1 Jeżeli liczba jest równa wylosowanej przerwij pętlę i przejdź do punktu 1.4
            if podana_liczba == wylosowana_liczba:
                break

            # 1.3.2 Jeżeli liczba jest większa od wylosowanej wyświetl komunikat, że liczba jest większa.
            elif podana_liczba > wylosowana_liczba:
                print("Podana liczba jest większa od wylosowanej.")

            # 1.3.3 Jeżeli liczba jest mniejsza od wylosowanej wyświetl komunikat, że liczba jest mniejsza.
            elif podana_liczba < wylosowana_liczba:
                print("Podana liczba jest mniejsza od wylosowanej.")

            # 1.3.4 Zwiększ liczbę prób o 1
            licznik_prob += 1

            # 1.3.5 Powróć do punktu 1.3 (pętla while True automatycznie wraca na początek)

        except ValueError:
            print("Błąd: Proszę wpisać poprawną liczbę całkowitą!")

    # Punkt 1.4 i 1.5 wykonają się dopiero po przerwaniu pętli (break w punkcie 1.3.1)
    print("\n--- Koniec gry ---")

    # 1.4 Wyświetl komunikat przedstawiający poprawną liczbę
    print(f"Brawo! Poprawna liczba to: {wylosowana_liczba}")

    # 1.5 Wyświetl komunikat przedstawiający ilość prób.
    print(f"Odgadłeś wylosowaną liczbę w {licznik_prob} próbie.")


# Uruchomienie programu
if __name__ == "__main__":
    gra_w_zgadywanie()