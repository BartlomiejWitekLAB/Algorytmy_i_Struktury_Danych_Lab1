def czy_palindrom(napis):
    # 1. Warunek bazowy:
    # Jeśli napis ma długość 0 lub 1, to z definicji jest palindromem.
    # Właśnie w tym miejscu nasza rekurencja się zatrzyma.
    if len(napis) <= 1:
        return True

    # 2. Sprawdzanie skrajnych liter:
    # Porównujemy pierwszy znak (indeks 0) z ostatnim znakiem (indeks -1).
    if napis[0] != napis[-1]:
        # Jeśli się różnią, to na pewno nie jest to palindrom.
        return False

    # 3. Wywołanie rekurencyjne:
    # Skoro pierwsza i ostatnia litera są takie same, to odcinamy je
    # i wywołujemy tę samą funkcję dla "środka" wyrazu.
    # Używamy wycinania (slicing) [1:-1], co oznacza "weź znaki od drugiego do przedostatniego".
    return czy_palindrom(napis[1:-1])


# ==========================================
# Testowanie programu
# ==========================================

print("--- TESTY FUNKCJI REKURENCYJNEJ ---")

print(f'czy_palindrom("kajak")  -> {czy_palindrom("kajak")}')
print(f'czy_palindrom("radar")  -> {czy_palindrom("radar")}')
print(f'czy_palindrom("python") -> {czy_palindrom("python")}')
print(f'czy_palindrom("anna")   -> {czy_palindrom("anna")}')