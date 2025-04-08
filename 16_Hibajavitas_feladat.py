#
# 16_Hibajavitas_feladat
#
"""
Javítsd a hibát, hogy működjön a számkitalálós játék!
"""

import random

szam = random.randint(1, 5)
tipp = int(input("Tippelj egy számot 1 és 5 között: "))

if tipp = szam:
    print("Eltaláltad!")
else:
    print("Sajnos nem talált.")


"""
A felhasználó pontszáma alapján írjuk ki a megfelelő értékelést!
"""

pont = int input("Hány pontot szereztél? (0-100): "))

if pont >= 90:
    print("Jeles")
elif pont >= 70
    print("Közepes")
else:
print("Sikertelen")



"""
Kérdezzük le az életkort, és írjuk ki, hogy beléphet-e (18+).
"""

kor = input("Hány éves vagy? ")

if kor >= 18:
    print("Beléphetsz.")
else:
    print("Sajnálom, még kiskorú vagy.")