#
# 14_Hibajavitas_megoldva
#
"""
Javítsd ki a hibákat, hogy helyesen kiszámolja a számok összegét!
"""

szamok = [3, 5, 8, 2, 6]
osszeg = 0
for szam in szamok:
    osszeg += szam  # HIBA: osszeg = szam helyett

print("A számok összege:", osszeg)


"""
Javítsd ki a hibát, hogy a program kiszámolja a lista elemeinek átlagát!
"""

szamok = [10, 20, 30, 40]
ossz = 0
for szam in szamok:
    ossz += szam  # HIBA: változónév jó, de figyelni kell rá

atlag = ossz / len(szamok)
print("Az átlag:", atlag)  # HIBA: 'átlag' helyett 'atlag' (accentos karakter)


"""
Javítsd ki a hibát, hogy a program megtalálja a legkisebb számot a listában!
"""

szamok = [12, 5, 8, 3, 15]
legkisebb = szamok[0]  # HIBA: kezdetben 0 volt, ami félrevezető lehet, ha a lista pozitív
for szam in szamok:
    if szam < legkisebb:
        legkisebb = szam

print("A legkisebb szám a listában:", legkisebb)