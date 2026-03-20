import math


def rownanie_kwadratowe(a, b, c):
    print(f"Równanie: {a}x^2 + {b}x + {c} = 0")

    # Krok 3: Sprawdzenie, czy to w ogóle równanie kwadratowe
    if a == 0:
        print("Błąd: Współczynnik 'a' wynosi 0, to nie jest równanie kwadratowe.")
        print("-" * 40)
        return

    # Krok 4: Obliczenie delty
    delta = b ** 2 - 4 * a * c
    print(f"Delta wynosi: {delta}")

    # Krok 5: Sprawdzenie czy delta > 0 (dwa pierwiastki)
    if delta > 0:
        pierwiastek_z_delty = math.sqrt(delta)
        x1 = (-b - pierwiastek_z_delty) / (2 * a)
        x2 = (-b + pierwiastek_z_delty) / (2 * a)
        print(f"Wynik: Równanie ma dwa różne pierwiastki rzeczywiste:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    # Krok 6: Sprawdzenie czy delta == 0 (jeden pierwiastek)
    elif delta == 0:
        x0 = -b / (2 * a)
        print(f"Wynik: Równanie ma jeden pierwiastek podwójny:")
        print(f"x0 = {x0}")

    # Krok 7 i 8: delta < 0 (brak pierwiastków)
    else:
        print("Wynik: Brak pierwiastków rzeczywistych (delta ujemna).")

    print("-" * 40)


# ==========================================
# 4. Testowanie programu dla różnych wartości
# ==========================================

print("--- TESTY PROGRAMU ---\n")

# Przypadek 1: Dwa różne pierwiastki (np. x^2 - 5x + 6 = 0, delta = 1)
rownanie_kwadratowe(1, -5, 6)

# Przypadek 2: Jeden pierwiastek podwójny (np. x^2 - 4x + 4 = 0, delta = 0)
rownanie_kwadratowe(1, -4, 4)

# Przypadek 3: Brak pierwiastków rzeczywistych (np. x^2 + x + 1 = 0, delta = -3)
rownanie_kwadratowe(1, 1, 1)

# Przypadek 4: Współczynnik a = 0 (zabezpieczenie)
rownanie_kwadratowe(0, 5, 2)