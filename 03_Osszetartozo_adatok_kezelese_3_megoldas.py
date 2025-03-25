"""
Összetartozó adatok kezelése

<<< 3.FELADAT >>>

a,Hozz létre egy listát, amely 10 darab véletlenszerű egész számot tartalmaz 1 és 100 között!
  Ehhez használd a random könyvtárat!
b,Írasd ki a generált listát!
  Számítsd ki és írasd ki:
c,A lista legkisebb számát
d,A lista legnagyobb számát
e,A lista elemeinek összegét
f,A lista elemeinek átlagát (összeg osztva az elemek számával)
  Extra feladat (ha van időd):
g,Írasd ki a lista elemeit növekvő sorrendben!

Tippek:

a,Használj import random és random.randint(1, 100) függvényt a véletlenszám-generáláshoz!
b,c,d,e,f,Használj min(), max(), sum(), és len() függvényeket a számításokhoz!
g,Használj sorted() függvényt a lista rendezéséhez!


"""
# import a Véletlenszám-generáláshoz
import random  

# Véletlen számok generálása és listába mentése
szamok = []
for z in range(10):
    randomszam = random.randint(1,100)
    szamok.append(randomszam)

# Lista kiíratása
print("A generált számok:", szamok)

# Legkisebb és legnagyobb szám keresése
print("Legkisebb szám:", min(szamok))
print("Legnagyobb szám:", max(szamok))

# Összeg és átlag számítása
osszeg = sum(szamok)
atlag = osszeg / len(szamok)
print("A számok összege:", osszeg)
print("A számok átlaga:", round(atlag, 2))

# Extra: Rendezett lista kiíratása
print("Számok növekvő sorrendben:", sorted(szamok))

