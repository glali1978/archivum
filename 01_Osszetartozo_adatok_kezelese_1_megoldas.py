"""
Összetartozó adatok kezelése

<<< 1.FELADAT >>>

a, Hozz létre egy üres listát, amelyben számokat fogsz tárolni!
b, Kérj be a felhasználótól 5 egész számot!
c, Minden bevitt számot adj hozzá a listához!
d, A bekérés után írasd ki a listát a képernyőre!
e, Extra feladat (ha van időd): Írasd ki a listában szereplő számok összegét is!

"""
#  Üres lista létrehozása
szamok = []

# 5 szám bekérése a felhasználótól
for i in range(5):
    szam = int(input())
    szamok.append(szam)  # Szám hozzáadása a listához

# Lista kiíratása
print("A megadott számok:", szamok)

# Extra feladat: számok összege
osszeg = sum(szamok)
print("A számok összege:", osszeg)
