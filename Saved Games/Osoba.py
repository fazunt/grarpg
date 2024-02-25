class Osoba:
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres
        self.data_urodzenia = data_urodzenia
        self.telefon = telefon

    def przedstaw_sie(self):
        return f"Jestem {self.imie} {self.nazwisko} , mój adres to {self.adres},urodziłem sie {self.data_urodzenia} , mój numer telefonu to {self.telefon} ."