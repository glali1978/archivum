#*************************************
#*************************************
# idojaras.py
#*************************************
#*************************************
from seged import leker_idojaras
#
#
"""
Ebben a feladatban egy LISTA-ban megadott városokról fogunk időjárási adatokat lekérni az internetről.
A letöltést végző részt már előkészítettük számodra egy segédfüggvény formájában 
neked csak a listákkal és ciklusokkal kell dolgoznod.

Dolgozd fel a megadott városok listáját.

Minden városhoz kérd le az időjárási adatokat a leker_idojaras() függvénnyel.

Írd ki minden városhoz:

a hőmérsékletet (°C),
az időjárás leírását (pl. „derült”),
a páratartalmat (%).


Amit használnod kell:
Lista városnevekkel
for ciklus, hogy végigmenj a listán
A már elkészített leker_idojaras(városnév) függvény, ami egy listát ad vissza:
["hőmérséklet", "leírás", "páratartalom"]


Tipp:
A függvény hívása így néz ki:

adat = leker_idojaras("Budapest")
Ezután például:

print(adat[0])  # hőmérséklet
print(adat[1])  # időjárás leírás
print(adat[2])  # páratartalom
"""




varosok = ["Budapest", "London", "Berlin", "Madrid", "Róma"]

#itt járjuk körbe for ciklussal a varosok LISTA-t

    #lekerjuk az idojaras adatokat az egyes városokra
 
    #kiírajuk az eredmeny LISTA elemeit
 