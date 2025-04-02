#*************************************
#*************************************
# 10_idojaras_megoldva.py
#*************************************
#*************************************
from seged import leker_idojaras
#
#
"""
Ebben a feladatban egy LISTA-ban megadott városokról fogunk időjárási adatokat lekérni az internetről.
A letöltést végző részt már előkészítettük számodra egy segédfüggvény formájában 
neked csak a listákkal és ciklusokkal kell dolgoznod.

Minden a megadott varosok[] LISTA-ban lévő városhoz kérd le az időjárási adatokat a leker_idojaras() függvénnyel.

Írd ki minden városhoz:

-a hőmérsékletet (°C),
-az időjárás leírását (pl. „derült”),
-a páratartalmat (%).


Amit használnod kell:
Lista városnevekkel
for ciklus, hogy végigmenj a listán
A már elkészített adat=leker_idojaras(városnév) függvény, ami egy listát ad vissza:
adat = ["hőmérséklet", "leírás", "páratartalom"]


adat = leker_idojaras("Budapest")
Ezután például:

print(adat[0])  # hőmérséklet
print(adat[1])  # időjárás leírás
print(adat[2])  # páratartalom

Ha működik próbáld ki a varosok["Budapest", ....] listát kedvenc városaiddal bővítve
"""




varosok = ["Budapest", "London", "Berlin", "Madrid", "Róma"]

#itt járjuk körbe for ciklussal a varosok LISTA-t
for varos in varosok:
    #lekerjuk az idojaras adatokat az egyes városokra
    adat = leker_idojaras(varos)
    #kiírajuk az eredmeny LISTA elemeit
    print(f"{varos}: {adat[0]} °C, {adat[1]}, páratartalom: {adat[2]}%")