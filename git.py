import math

#  sześcianu
def objetosc_sześcianu(a):
    return a**3

#  prostopadłościanu
def objetosc_prostopadloscianu(a, b, c):
    return a * b * c

#  stożka
def objetosc_stozka(r, h):
    return (1/3) * math.pi * r**2 * h

#  walca
def objetosc_walcu(r, h):
    return math.pi * r**2 * h

#  kuli
def objetosc_kuli(r):
    return (4/3) * math.pi * r**3

#  sfery
def objetosc_sfery(r):
    return (4/3) * math.pi * r**3

# piramidy
def objetosc_piramidy(base_area, h):
    return (1/3) * base_area * h

# graniastosłupa
def objetosc_graniastoslupa(base_area, h):
    return base_area * h

# torusa 
def objetosc_torusa(R, r):
    return 2 * math.pi**2 * R * r**2

# elipsoidy
def objetosc_elipsoidy(a, b, c):
    return (4/3) * math.pi * a * b * c


print("Objętość sześcianu:", objetosc_sześcianu(5))
print("Objętość prostopadłościanu:", objetosc_prostopadloscianu(3, 4, 5))
print("Objętość stożka:", objetosc_stozka(2, 4))
print("Objętość walca:", objetosc_walcu(3, 6))
print("Objętość kuli:", objetosc_kuli(4))
print("Objętość sfery:", objetosc_sfery(3))
print("Objętość piramidy:", objetosc_piramidy(10, 4))
print("Objętość graniastosłupa:", objetosc_graniastoslupa(8, 6))
print("Objętość torusa:", objetosc_torusa(5, 2))
print("Objętość elipsoidy:", objetosc_elipsoidy(4, 3, 2))