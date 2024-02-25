from Osoba import Osoba

class Konsultanci(Osoba):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, specjalizacja):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.specjalizacja = specjalizacja
        self.historia_projektow = []
        self.raporty_doradcze = []

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Moja specializacją jest {self.specjalizacja}"