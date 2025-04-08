#
# 16_Hibajavitas_megoldva
#
import random

szam = random.randint(1, 5)
tipp = int(input("Tippelj egy számot 1 és 5 között: "))

if tipp == szam:  # HIBA: = helyett ==
    print("Eltaláltad!")
else:
    print("Sajnos nem talált.")



pont = int(input("Hány pontot szereztél? (0-100): "))

if pont >= 90:
    print("Jeles")
elif pont >= 70:  # HIBA: kettőspont hiányzott
    print("Közepes")
else:
    print("Sikertelen")




kor = int(input("Hány éves vagy? "))  # HIBA: stringet kaptunk, szám kell

if kor >= 18:
    print("Beléphetsz.")
else:
    print("Sajnálom, még kiskorú vagy.")
