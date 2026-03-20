def policz_parzyste():
    print("--- Program do zliczania liczb parzystych ---")

    # Wczytywanie długości ciągu (n)
    while True:
        try:
            n = int(input("Podaj długość ciągu n (n > 0): "))
            if n > 0:
                break
            else:
                print("Błąd: Liczba n musi być większa od zera!")
        except ValueError:
            print("Błąd: Podaj poprawną liczbę całkowitą!")

    licznik_parzystych = 0

    # Pętla wczytująca n liczb
    for i in range(1, n + 1):
        while True:
            try:
                liczba = int(input(f"Podaj liczbę nr {i}: "))
                break  # Jeśli poprawna liczba, wychodzimy z wewnętrznej pętli while
            except ValueError:
                print("Błąd: Podaj poprawną liczbę całkowitą!")

        # Sprawdzanie parzystości
        if liczba % 2 == 0:
            licznik_parzystych += 1

    # Wyświetlenie wyniku
    print("\n--- Podsumowanie ---")
    print(f"W podanym ciągu znajduje się {licznik_parzystych} liczb parzystych.")


# Uruchomienie programu
if __name__ == "__main__":
    policz_parzyste()