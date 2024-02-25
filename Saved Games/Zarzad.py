from Osoba import Osoba

class Zarzad(Osoba):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, stanowisko):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.stanowisko = stanowisko
        self.decyzje_strategiczne = []
        self.raporty_finansowe = []

    def przedstaw_sie(self):
            return super().przedstaw_sie() + f" Moim stanowiskiem jest {self.stanowisko}"
