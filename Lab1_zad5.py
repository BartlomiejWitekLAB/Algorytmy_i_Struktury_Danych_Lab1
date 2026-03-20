def druga_najwieksza(lista):
    # 1. Zamieniamy listę na zbiór (set), co automatycznie usuwa wszystkie duplikaty.
    # Następnie zamieniamy zbiór z powrotem na listę.
    unikalne_wartosci = list(set(lista))

    # 2. Sortujemy listę malejąco (od największej do najmniejszej liczby).
    unikalne_wartosci.sort(reverse=True)

    # 3. Ponieważ lista jest posortowana malejąco i nie ma duplikatów,
    # druga największa liczba znajduje się zawsze pod indeksem 1.
    return unikalne_wartosci[1]


# ==========================================
# Testowanie programu
# ==========================================

print("--- TESTY FUNKCJI ---")

# Przykład 1 z zadania
lista1 = [10, 20, 4, 45, 99, 99]
wynik1 = druga_najwieksza(lista1)
print(f"lista = {lista1}")
print(f"druga_najwieksza(lista) -> {wynik1}\n")

# Przykład 2 z zadania
lista2 = [1, 2, 3, 4, 5]
wynik2 = druga_najwieksza(lista2)
print(f"lista = {lista2}")
print(f"druga_najwieksza(lista) -> {wynik2}\n")

# Przykład 3 z zadania
lista3 = [10, 10, 10, 9]
wynik3 = druga_najwieksza(lista3)
print(f"lista = {lista3}")
print(f"druga_najwieksza(lista) -> {wynik3}\n")

# Mój dodatkowy test z liczbami ujemnymi
lista4 = [-5, -10, -2, -2, -1]
wynik4 = druga_najwieksza(lista4)
print(f"lista = {lista4}")
print(f"druga_najwieksza(lista) -> {wynik4}")