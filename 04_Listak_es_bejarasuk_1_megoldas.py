"""
Listák és bejárásuk

<<< 1.FELADAT >>>

Dolgozat pontszámok elemzése

Készíts egy programot, amely bekéri egy osztály dolgozatpontszámait!

A program:
Kérje be a tanulók pontszámait addig, amíg a felhasználó üres enterrel nem zárja le a bevitelét.
a, Minden új pontszám megadása után írja ki az eddig megadott pontokat!
   A végén írja ki:
b, A legjobb és a leggyengébb eredményt
c, Az átlagpontszámot
d, Az összes pontot növekvő sorrendben

Tippek:
a, print("Valamiszöveg=", ", ".join(map(str, lista)))
b, min(lista) , max(lista)
c, sum(lista) / len(lista)
d, mint az "a," pont csak rendezve: sorted(lista)

"""
# Üres lista a pontszámok tárolására
pontszamok = []

while True:
    # Pontszámok kiíratása
    print("Eddigi pontszámok:", ", ".join(map(str, pontszamok)))
    
    # Pontszám bekérése
    pont = input("Kérem egy tanuló pontszámát (vagy üres enter a befejezéshez): ")
    if pont == '':
        break  # Kilépés, ha nincs új pontszám
    pont = int(pont)
    pontszamok.append(pont)

# Ha van adat, akkor eredmények kiíratása
if pontszamok:
    print("\nEredmények:")
    print(f"Legjobb pontszám: {max(pontszamok)}")
    print(f"Leggyengébb pontszám: {min(pontszamok)}")
    print(f"Átlagpontszám: {sum(pontszamok) / len(pontszamok)}")
    print("Pontszámok növekvő sorrendben:", ", ".join(map(str, sorted(pontszamok))))
else:
    print("\nNem adtál meg pontszámokat!")