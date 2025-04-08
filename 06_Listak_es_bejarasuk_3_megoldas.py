"""
Listák és bejárásuk

<<< 3.FELADAT >>>

Magasságok elemzése

Egy osztály diákjainak magasságát kell rögzíteni és elemezni. A program:

a,Először megkérdezi, hány diák magasságát szeretnéd bevinni. (while ciklus, hogy csak érvényes számot fogadjon el!)
b,Ezután egy for ciklusban bekéri az egyes diákok magasságát (cm-ben).
c,Minden új magasság megadása után kiírja az eddigi adatokat.
  A végén kiszámítja és kiírja:
d,A legmagasabb és legalacsonyabb diákot
e,Az átlagmagasságot
f,A magasságokat növekvő sorrendben

Extra Feladat: Gondoskodj róla hogy az adat ki, illetve bemenetek hibatűrőek legyenek! 0-val való osztás vizsgálata stb...

Tippek:
a, szam = int(input("Kérdés? "))
b, for ciklus range(1, szam + 1):
c, print("Valamiszöveg=", ", ".join(map(str, lista)))
d, min(lista) , max(lista)
e, sum(lista) / len(lista)
f, mint az "a," pont csak rendezve: sorted(lista)

"""
# Üres lista a magasságok tárolására
magassagok = []

# Bekérjük, hány diák magasságát kell megadni (while a helyes inputért)
while True:
    try:
        n = int(input("Hány diák magasságát szeretnéd megadni? "))
        if n > 0:
            break
        else:
            print("Adj meg egy pozitív egész számot!")
    except ValueError:
        print("Hibás bevitel! Kérlek, egész számot adj meg!")

# For-ciklussal bekérjük az adatokat
for i in range(1, n + 1):
    magassag = int(input(f"Kérem az {i}. diák magasságát (cm): "))
    magassagok.append(magassag)

    # Eddigi magasságok kiíratása
    print("Eddigi magasságok:", ", ".join(map(str, magassagok)))

# Eredmények kiíratása
print("\nEredmények:")
print(f"Legalacsonyabb diák: {min(magassagok)} cm")
print(f"Legmagasabb diák: {max(magassagok)} cm")
print(f"Átlagmagasság: {round(sum(magassagok) / len(magassagok), 2)} cm")
print("Magasságok növekvő sorrendben:", ", ".join(map(str, sorted(magassagok))))