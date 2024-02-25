from Osoba2 import Osoba2


class Admin(Osoba2):
    def __init__(self, imie, nazwisko, adres, data_urodzenia, telefon, login, haslo, poziom_uprawnien):
        super().__init__(imie, nazwisko, adres, data_urodzenia, telefon)
        self.login = login
        self.haslo = haslo
        self.poziom_uprawnien = poziom_uprawnien

    def przedstaw_sie(self):
        return super().przedstaw_sie() + f" Moim poziomem uprawnienia jest {self.poziom_uprawnien}"