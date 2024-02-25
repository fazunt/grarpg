from Osoba2 import Osoba2

class Ksiegowi(Osoba2):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, umiejetnosci_ksiegowe):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.umiejetnosci_ksiegowe = umiejetnosci_ksiegowe
        self.transakcje_finansowe = []
        self.bilanse = []

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Moje umiejetności księgowe to {self.umiejetnosci_ksiegowe}"
