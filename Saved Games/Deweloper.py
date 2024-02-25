from Osoba import Osoba

class Deweloper(Osoba):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, umiejetnosci_programistyczne):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.umiejetnosci_programistyczne = umiejetnosci_programistyczne
        self.projekty = []

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Moje umiejetności programistyczne obejmuja {self.umiejetnosci_programistyczne}."
    