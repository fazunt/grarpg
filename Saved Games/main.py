from Admin import Admin
from Klienci import Klienci
from Deweloper import Deweloper
from HRowiec import HRowiec
from Zarzad import Zarzad
from Ksiegowi import Ksiegowi
from Konsultanci import Konsultanci
    
klient1 = Klienci("Jan", "Kowalski", "ul. Kwiatowa 5", "1990-05-15", "123-456-789", "12345")
admin1 = Admin("Anna", "Nowak", "ul. Słoneczna 10", "1985-12-10", "987-654-321", "admin", "haslo123", "administrator")
deweloper1 = Deweloper("Adam", "Wiśniewski", "ul. Leśna 7", "1988-08-20", "456-789-012", ["Python", "JavaScript"])
hrowiec1 = HRowiec("Katarzyna", "Kowalczyk", "ul. Brzozowa 2", "1975-03-28", "111-222-333", "2010-05-10")
zarzad1 = Zarzad("Piotr", "Nowakowski", "ul. Lipowa 11", "1960-10-15", "999-888-777", "Prezes")
ksiegowy1 = Ksiegowi("Maria", "Lewandowska", "ul. Dębowa 3", "1982-06-05", "555-444-333", "księgowość podatkowa")
konsultant1 = Konsultanci("Tomasz", "Kowal", "ul. Akacjowa 8", "1995-11-20", "777-666-555", "analiza biznesowa")


print(klient1.przedstaw_sie())
print(admin1.przedstaw_sie())
print(deweloper1.przedstaw_sie())
print(hrowiec1.przedstaw_sie())
print(zarzad1.przedstaw_sie())
print(ksiegowy1.przedstaw_sie())
print(konsultant1.przedstaw_sie())
    
