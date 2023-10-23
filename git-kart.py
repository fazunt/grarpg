# 1..................................................................

tablica_A = [1, 7, 14, 21, 28, 5, 35, 42, 10, 49]
tablica_podzielne_przez_7 = []
tablica_niepodzielne_przez_7 = []

for liczba in tablica_A:
    if liczba % 7 == 0:
        tablica_podzielne_przez_7.append(liczba)
    else:
        tablica_niepodzielne_przez_7.append(liczba)

print("Tablica z liczbami podzielnymi przez 7:", tablica_podzielne_przez_7)
print("Tablica z liczbami niepodzielnymi przez 7:", tablica_niepodzielne_przez_7)


# 2..................................................................


def suma_podzielnych_przez_a(tablica, a):
    suma = 0
    for liczba in tablica:
        if liczba % a == 0:
            suma += liczba
    return suma

tablica_A = [1, 7, 14, 21, 28, 5, 35, 42, 10, 49]
a = 7

suma = suma_podzielnych_przez_a(tablica_A, a)
print(f"Suma liczb podzielnych przez {a} wynosi: {suma}")


# 3..................................................................


def liczba_wystapien(tablica, element):
    licznik = 0
    for item in tablica:
        if item == element:
            licznik += 1
    return licznik

tablica_A = [1, 7, 14, 7, 28, 5, 35, 42, 10, 7]
element_do_sprawdzenia = 7

ilosc_wystapien = liczba_wystapien(tablica_A, element_do_sprawdzenia)
print(f"Element {element_do_sprawdzenia} występuje {ilosc_wystapien} razy w tablicy.")


# 4..................................................................


def indeksy_minimalnych_wartosci(tablica):
    minimalne_wartosci = min(tablica)
    indeksy = [indeks for indeks, el in enumerate(tablica) if el == minimalne_wartosci]
    return indeksy

tablica_A = [10, 5, 8, 2, 5, 1, 8, 2, 3]
indeksy_minimalnych = indeksy_minimalnych_wartosci(tablica_A)

print(f"Minimalne wartości znajdują się pod indeksami: {indeksy_minimalnych}")


# 5.................................................................


def srednia_harmoniczna(liczby):
    suma_odwrotnosci = sum(1 / liczba for liczba in liczby)
    srednia_harm = len(liczby) / suma_odwrotnosci
    return srednia_harm

liczby = []

while True:
    try:
        liczba = float(input("Podaj liczbę (wpisz 'koniec' aby zakończyć): "))
        liczby.append(liczba)
    except ValueError:
        print("Nieprawidłowa liczba. Wprowadź liczbę lub 'koniec' aby zakończyć.")

    if input("Czy chcesz wprowadzić kolejną liczbę? (Tak/Nie): ").strip().lower() != 'tak':
        break

if len(liczby) > 0:
    srednia = srednia_harmoniczna(liczby)
    print(f"Średnia harmoniczna wprowadzonych liczb to: {srednia:.2f}")
else:
    print("Nie podano żadnych liczb.")


# 6.................................................................


import math

tablica_A = [1, 3, 4, 7, 9, 12, 16, 25, 36, 49, 53, 64, 81, 100]
tablica_calkowitopierwiastkowych = []
tablica_innych = []

for liczba in tablica_A:
    pierwiastek = math.sqrt(liczba)  # Oblicz pierwiastek kwadratowy
    if pierwiastek.is_integer():
        tablica_calkowitopierwiastkowych.append(liczba)
    else:
        tablica_innych.append(liczba)

print("Liczby z pierwiastkiem całkowitym:", tablica_calkowitopierwiastkowych)
print("Pozostałe liczby:", tablica_innych)
