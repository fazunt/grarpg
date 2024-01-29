    
import uuid


ksiazka1 = {
        'nazwa': 'Cień wiatru',
        'ilość stron': '512',
        'autor': 'Carlos Ruiz Zafón',
        'id': uuid.uuid4()
    }

ksiazka2 = {
        'nazwa': 'Dziewczyna z pociągu',
        'ilość stron': '325',
        'autor': 'Paula Hawkins',
        'id': uuid.uuid4()
    }

ksiazka3 = {
        'nazwa': 'Władca Pierścieni: Drużyna Pierścienia',
        'ilość stron': '576',
        'autor': 'J.R.R. Tolkien',
        'id': uuid.uuid4()
    }

biblioteka = [ksiazka1, ksiazka2, ksiazka3]

def informacje_o_ksiazce(ksiazka):
    for k, v in ksiazka.items():
        print(f"{k}: {v}")
    print("===" * 20)

def dodaj_nowa_ksiazke(biblioteka):
    x = input("Podaj tytuł: ")
    y = input("Podaj liczbę stron: ")
    z = input("Podaj autora: ")
    nowa_ksiazka = {
        'nazwa': x,
        'ilość stron': y,
        'autor': z,
        'id': uuid.uuid4()
    }
    biblioteka.append(nowa_ksiazka)
    print("Nowa książka dodana pomyślnie.")

def czy_ksiazka_istnieje(lista, id):
    for i in range(len(lista)):
        if str(lista[i]["id"]) == id:
            return True
    return False

def indeks_ksiazki(lista, id):
    for i in range(len(lista)):
        if str(lista[i]["id"]) == id:
            return i
    return -1

def usun_ksiazke(lista):
    id_do_usuniecia = input("Podaj ID książki do usunięcia: ")
    if czy_ksiazka_istnieje(lista, id_do_usuniecia):
        indeks = indeks_ksiazki(lista, id_do_usuniecia)
        if indeks != -1:
            lista.pop(indeks)
            print("Książka usunięta pomyślnie.")
        else:
            print("Nie ma takiej książki.")
    else:
        print("Nie ma takiej książki.")

def edytuj_ksiazke(lista):
    id_do_edytowania = input("Podaj ID książki do edycji: ")
    if czy_ksiazka_istnieje(lista, id_do_edytowania):
        indeks = indeks_ksiazki(lista, id_do_edytowania)
        if indeks != -1:
            pole_do_edytowania = input("Podaj pole do edycji: ")
            lista[indeks][pole_do_edytowania] = input("Podaj nową wartość: ")
            print(f"{pole_do_edytowania} zaktualizowane pomyślnie.")
        else:
            print("Nie ma takiej książki.")
    else:
        print("Nie ma takiej książki.")

while True:
        print("i - informacje")
        print("e - edytuj dane")
        print("d - dodaj książkę")
        print("u - usuń książkę")
        print("q - wyjście")
        dzialanie = input("Wybierz akcję: ")

        if dzialanie == "i":
            for ksiazka in biblioteka:
                informacje_o_ksiazce(ksiazka)
        elif dzialanie == "e":
            edytuj_ksiazke(biblioteka)
        elif dzialanie == "d":
            dodaj_nowa_ksiazke(biblioteka)
        elif dzialanie == "u":
            usun_ksiazke(biblioteka)
        elif dzialanie == "q":
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")