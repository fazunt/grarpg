from random import randint

Namew = "Ninja"
hp_ninja = 5
atak_ninja = randint(2,3)
ninja = [Namew,hp_ninja,atak_ninja]

Nameq = "Sigma"
hp_sigma = 3
atak_sigma = randint(1,2)  
sigma = [Nameq,hp_sigma,atak_sigma]

Namet = "Gigachad"
hp_gigachad = 10
atak_gigachad = randint(4,5)
gigachad = [Namet,hp_gigachad,atak_gigachad]

Nameg = "Buntownik"
hp_buntownik = 15
atak_buntownik = randint(5,7)
buntownik = [Nameg,hp_buntownik,atak_buntownik]

Namess = "Zolnierz"
hp_zolnierz = 5
atak_zolnierz = randint(5,10)
zolnierz = [Namess,hp_zolnierz,atak_zolnierz]

Namewoj = "Wojownik"
hp_woj = 8
atak_woj = randint(3,5)
wojownik = [Namewoj,hp_woj,atak_woj]

Names = "Bokser"
hp_bokser = 20
atak_bokser = randint(5,8)
bokser = [Names,hp_bokser,atak_bokser]

def ręka():
    atak = randint(1,3)
    return atak

def miecz():
    atak = randint(2,4)
    return atak

def noga():
    atak = randint(3,5)
    return atak

def siekiera():
    atak = randint(4,6)
    return atak

def pistolet():
    atak = randint(5,7)
    return atak

def wm():
    atak = randint(6,8)
    return atak

def wt():
    atak = randint(7,9)
    return atak

def poparz():
    global mana
    if mana > 5:
        mana -= 5
        atak = randint(3,5)
        return atak
    else:
        print("Nie masz many ")
        return 0

def lightsaber():
    global mana
    if mana > 10:
        mana -= 10
        atak = randint(4,6)
        return atak
    else:
        print("Nie masz many ")
        return 0

def fire_ball():
    global mana
    if mana > 20:
        mana -= 20
        atak = randint(5,7)
        return atak
    else:
        print("Nie masz many ")
        return 0

ataki =[
    {
"1 = Kopnięcie"
    },
    {
"2 = atak nożem",
    },
    {
"3 = uderzenie",
    },
]

def los():
    co = randint(1,7)
    if co == 1:
        pp = ninja
    elif co == 2:
        pp = sigma
    elif co == 3:
        pp = gigachad
    elif co == 4:
        pp = buntownik
    elif co == 7:
        pp = zolnierz
    elif co == 5:
        pp = wojownik
    elif co == 6:
        pp = bokser
    return pp

def wa():
    print(ataki)
    co = int(input())
    if co == 1:
        return ręka()
    elif co == 2:
            return noga()  
    elif co == 3:
        if mana > 5:
            return poparz()
        else:
            print("Nie masz many!!")
            return 0
    elif co == 4:
        return noga()
    elif co == 5:
        return siekiera()
    elif co == 6:
        return pistolet()
    elif co == 7:
        return wm()
    elif co == 8:
        return wt()
    elif co == 9:
        if mana > 10:
            return siekiera()
        else:
            print("Nie masz many!!")
            return 0
    elif co == 10:
        if mana > 20:
            return fire_ball()
        else:
            print("Nie masz many!!")
            return 0
    else:
        print("Nie wybrano akcji")
        return 0

def nagroda():
    new_dictionary = {}
    dw=int(input("""Witaj! W nagrodę za twoje czyny możesz wybrać nagrodę.
    1 = SigmaBat
    2 = GigachadBat
    3 = KarabinZolnierza
    4 = KlawiaturaBuntownika
    5 = BandanaNindzy
    6 = RekawiceBokserskie
    7 = OgnistaKula
    """))
    while True:
        if dw == 1:
            SigmaBat = "sigmabat"
            new_dictionary["4 = "] = SigmaBat if SigmaBat else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 2:
            GigachadBat = "GigachadBat"
            new_dictionary["5 = "] = GigachadBat if GigachadBat else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 3:
            KarabinZolnierza = "KarabinZolnierza"
            new_dictionary["6 = "] = KarabinZolnierza if KarabinZolnierza else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 4:
            KlawiaturaBuntownika = "KlawiaturaBuntownika"
            new_dictionary["7 = "] = KlawiaturaBuntownika if KlawiaturaBuntownika else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 5:
            BandanaNindzy = "BandanaNindzy"
            new_dictionary["8 = "] = BandanaNindzy if BandanaNindzy else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 6:
            RekawiceBokserskie = "RekawiceBokserskie"
            new_dictionary["9 = "] = RekawiceBokserskie if RekawiceBokserskie else "No data"
            ataki.append(new_dictionary)
            break
        elif dw == 7:
            OgnistaKula = "OgnistaKula"
            new_dictionary["10 = "] = OgnistaKula if OgnistaKula else "No data"
            ataki.append(new_dictionary)
            break
        else:
            print("Brak broni pod danym numerem. Spróbuj ponownie.")
            return 0   

życie = 100
mana = 100
name = input("Jak się nazywasz: ")
print(F"Witaj {name}! Twoim zadaniem będzie zyskanie chwały. Powodzenia szefie!")
wynik = 0
while życie > 0:
    przeciwnik = los()
    while przeciwnik[1] > 0:
        print(f"{name} walczy teraz z {przeciwnik[0]}")
        print(f"Przeciwnik ma aktualnie {przeciwnik[1]} hp i zadaje ci {przeciwnik[2]} obrażeń")
        życie = życie - przeciwnik[2]
        if życie < 0:
            break
        print(f"Zostało ci {życie} hp i {mana} many")
        atak  = wa()
        przeciwnik[1] = przeciwnik[1] - atak
        print(f"Zadałeś {atak} obrażeń")
    print('Zabiłeś przeciwnika!!!')
    wynik += 1
    if wynik % 5 == 0:
        nagroda()
else:
    print("Giniesz!")
print(f"Pokonałeś {wynik} przeciwników")