def znajdz_min_max(macierz):
    # Proste zabezpieczenie na wypadek pustej macierzy
    if not macierz or not macierz[0]:
        print("Macierz jest pusta.")
        return

    # 1. Inicjalizacja zmiennych
    # Na start zakładamy, że pierwszy element (wiersz 0, kolumna 0) jest zarówno naszym minimum, jak i maksimum.
    min_wartosc = macierz[0][0]
    max_wartosc = macierz[0][0]
    min_indeks = (0, 0)
    max_indeks = (0, 0)

    # 2. Przeszukiwanie macierzy w poszukiwaniu minimum i maksimum
    for i in range(len(macierz)):  # Iteracja po wierszach
        for j in range(len(macierz[i])):  # Iteracja po kolumnach w danym wierszu
            obecna_wartosc = macierz[i][j]

            # Sprawdzamy czy obecny element jest mniejszy od dotychczasowego minimum
            if obecna_wartosc < min_wartosc:
                min_wartosc = obecna_wartosc
                min_indeks = (i, j)

            # Sprawdzamy czy obecny element jest większy od dotychczasowego maksimum
            if obecna_wartosc > max_wartosc:
                max_wartosc = obecna_wartosc
                max_indeks = (i, j)

    # 3. Wyświetlenie macierzy ze zmienionymi wartościami
    print("Macierz:")
    for i in range(len(macierz)):
        wiersz_tekst = ""
        for j in range(len(macierz[i])):
            # Jeśli obecny indeks to indeks minimum, dodaj "MIN"
            if (i, j) == min_indeks:
                wiersz_tekst += f"{'MIN':>4} "
            # Jeśli obecny indeks to indeks maksimum, dodaj "MAX"
            elif (i, j) == max_indeks:
                wiersz_tekst += f"{'MAX':>4} "
            # W przeciwnym razie dodaj zwykłą liczbę
            else:
                wiersz_tekst += f"{macierz[i][j]:>4} "

        # Wypisz cały sklejony wiersz
        print(wiersz_tekst)


# ==========================================
# Testowanie programu
# ==========================================

# Dane wejściowe z zadania
macierz_testowa = [
    [5, 2, 9, 8],
    [1, 7, 3, 4],
    [6, 0, 2, 5]
]

# Wywołanie funkcji
znajdz_min_max(macierz_testowa)