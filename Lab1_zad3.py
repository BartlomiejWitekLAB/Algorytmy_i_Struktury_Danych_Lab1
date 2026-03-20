def wyszukaj_element():
    print("--- Program wyszukujący element w ciągu ---")

    # 1. Wczytywanie n > 0 z zabezpieczeniem przed błędami
    while True:
        try:
            n = int(input("Podaj ilość elementów ciągu n (n > 0): "))
            if n > 0:
                break
            else:
                print("Błąd: Liczba n musi być większa od zera!")
        except ValueError:
            print("Błąd: Podaj poprawną liczbę całkowitą!")

    # 2. Wczytywanie n elementów ciągu
    ciag = []
    print("\n--- Wprowadzanie elementów ciągu ---")
    for i in range(n):
        while True:
            try:
                element = int(input(f"Podaj element nr {i + 1}: "))
                ciag.append(element)
                break
            except ValueError:
                print("Błąd: Podaj poprawną liczbę całkowitą!")

    # 3. Pobranie liczby do wyszukania
    print("\n--- Wyszukiwanie ---")
    while True:
        try:
            szukana = int(input("Podaj liczbę do wyszukania w ciągu: "))
            break
        except ValueError:
            print("Błąd: Podaj poprawną liczbę całkowitą!")

    # 4 & 5. Sprawdzanie i szukanie indeksu pierwszego wystąpienia
    znaleziona = False
    indeks = -1

    for i in range(n):
        if ciag[i] == szukana:
            znaleziona = True
            indeks = i
            break # Przerywamy pętlę, bo interesuje nas tylko pierwsze wystąpienie!

    # Wyświetlanie wyniku
    print("\n--- Wynik ---")
    if znaleziona:
        print(f"Sukces! Liczba {szukana} występuje w ciągu.")
        print(f"Indeks jej pierwszego wystąpienia to: {indeks} (jest to {indeks + 1}. element wprowadzonego ciągu).")
    else:
        print(f"Niestety, liczba {szukana} nie występuje w podanym ciągu.")

# Uruchomienie programu
if __name__ == "__main__":
    wyszukaj_element()