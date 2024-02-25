from Osoba import Osoba

class Klienci(Osoba):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, numer_klienta):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.numer_klienta = numer_klienta
        self.historia_zamowien = []
        self.dane_platnosci = {}

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Mój numer klienta to {self.numer_klienta}"