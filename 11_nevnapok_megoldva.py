#*************************************
#*************************************
# 11_nevnapok_megoldva.py
#*************************************
#*************************************
from seged import leker_nevnap
#
#
"""
Feladat:
Adott egy ország- és dátum LISTA. 
Minden országnál kérdezd le az adott napra eső névnapot az internetről.
Használd a segédfüggvényt: nevek = leker_nevnap(orszag_kod, datum)

Minden országhoz és dátumhoz írd ki:
- ha van névnap: "Magyarország (03-25): Irén"
- ha nincs: "Németország (03-25): Nincs névnap"

Választható országok kódok listája, próbálj ki többet bővítsd az "adatok" LISTA-t:
    "at" "bg" "cz" "de" "dk" "ee" "es" "fi" "fr" "gr" "hr" "hu" "it" "lt" "lv" "pl" "ru" "se" "sk" "us"

"""

adatok = [
    ["hu", "03-25"],
    ["de", "03-25"],
    ["pl", "03-19"],
    ["sk", "03-25"],
    ["it", "03-25"]
]

# for ciklussal körbejárjuk az adatok LISTA-t
for elem in adatok:
     # a listában lévő elem[0]=ország, elem[1]=dátum
    orszag = elem[0]
    datum = elem[1]
    # ezekkel meghívjuk az internetről lekérő leker_nevnap függvényt
    nevek = leker_nevnap(orszag, datum)
    # vizsgáljuk hogy a függvény által visszakapott nevek hossza nagyobb > 0 
    if len(nevek) == 0:
        # Ha 0 hossza van Nincs névnap adat
        print(orszag, datum, ": Nincs névnap.")
    else:
        # kiírjuk az eredményt
        print(orszag, datum, nevek)
        print(f"{orszag.upper()} ({datum}): {', '.join(nevek)}")
