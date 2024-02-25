from Osoba2 import Osoba2

class HRowiec(Osoba2):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, historia_zatrudnienia):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.historia_zatrudnienia = historia_zatrudnienia
        self.dane_rekrutacyjne = {}
        self.dokumentacja_pracownikow = []

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" zatrudniliśmy cie {self.historia_zatrudnienia}"