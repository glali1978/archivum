"""
Listák és bejárásuk

<<< 2.FELADAT >>>


Egy osztály tanulói futóversenyen vettek részt. Írj egy programot, amely a versenyzők futási idejét (másodpercben) kéri be és elemzi!

A program:

a, Először kérdezze meg, hogy hány tanuló futási idejét kell rögzíteni.
b,Ezután for-ciklusban kérje be a tanulók futási idejét.
c,Minden új futási idő megadása után írja ki az eddig megadott futási időket!
  A végén írja ki:
d,A leggyorsabb (legkisebb) és leglassabb (legnagyobb) időt
e,Az átlagos futási időt
f,Az időket növekvő sorrendben


Tippek:
a, szam = int(input("Kérdés? "))
b, for ciklus range(1, szam + 1):
c, print("Valamiszöveg=", ", ".join(map(str, lista)))
d, min(lista) , max(lista)
e, sum(lista) / len(lista)
f, mint az "a," pont csak rendezve: sorted(lista)

"""
# Üres lista a futási idők tárolására
futasi_idok = []

# Bekérjük, hány időt szeretnénk rögzíteni
n = int(input("Hány futó idejét szeretnéd megadni? "))

# For-ciklussal bekérjük az adatokat
for i in range(1, n + 1):    
   ido = int(input(f"Kérem az {i}. futó idejét másodpercben: "))
   futasi_idok.append(ido)
    # Eddigi idők kiíratása
   print("Eddigi idők:", ", ".join(map(str, futasi_idok)))

# Eredmények kiíratása
print("\nEredmények:")
print(f"Leggyorsabb idő: {min(futasi_idok)} másodperc")
print(f"Leglassabb idő: {max(futasi_idok)} másodperc")
print(f"Átlagos futási idő: {sum(futasi_idok) / len(futasi_idok)} másodperc")
print("Idők növekvő sorrendben:", ", ".join(map(str, sorted(futasi_idok))))

