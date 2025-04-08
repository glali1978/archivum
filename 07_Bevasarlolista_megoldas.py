"""
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
<<<                                                       >>>
<<<          Bevásárlólista (Python gyakorlófeladat)      >>>
<<<                                                       >>>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Feladatleírás
Készíts programot, amely egy bevásárlólistát kezel!

Feladatok
a) A felhasználó addig adhat hozzá elemeket a listához, amíg nem írja be, hogy "STOP" (vagy "stop").
b) Minden új termék hozzáadása után a program írja ki az eddigi listát.
c) Ha a felhasználó üres sort ír be, a program figyelmeztesse, hogy nem lehet üres terméket hozzáadni!
d) A végén a program írja ki:
 Az összes terméket ABC-sorrendben
 Az összes terméket fordított sorrendben
 Hány termék van a listán

 Extra kihívás:
A program ne engedje duplikált elemek hozzáadását!"

Tipp a megoldáshoz
a) Használjunk egy végtelen ciklust (while True), amely addig fut, amíg a felhasználó "STOP"-ot nem ír.
b) Egy lista (bevásárlólista) tárolja az elemeket.
c) Az üres inputokat egy if feltétellel kiszűrhetjük.
d) A sorted() függvény ABC-sorrendet ad, a sorted(..., reverse=True) pedig fordított sorrendet.

"""
# Üres lista a bevásárlólista tárolására
bevasarlolista = []

print("Adj hozzá termékeket a bevásárlólistához! Írd be, hogy 'STOP', ha befejezted.")

while True:
    termek = input("Termék neve: ").strip()  # Bevitel és felesleges szóközök levágása

    # Ha a felhasználó beírja, hogy "STOP" vagy "stop", akkor kilépünk a ciklusból
    if termek.lower() == "stop":
        break

    # Ha az input üres, hibaüzenet
    if termek == "":
        print("Nem adhatsz hozzá üres terméket!")
        continue

    # Ha a termék már szerepel a listában
    if termek in bevasarlolista:
        print("Ez a termék már szerepel a listában!")
        continue

    # Termék hozzáadása a halmazhoz
    bevasarlolista.append(termek)
    
    # Jelenlegi lista kiírása
    print("Bevásárlólista:", ", ".join(sorted(bevasarlolista)))

# Végső eredmények kiíratása
print("\n Bevásárlólista összegzése:")
print(f" ABC-sorrendben: {', '.join(sorted(bevasarlolista))}")
print(f" Fordított sorrendben: {', '.join(sorted(bevasarlolista, reverse=True))}")
print(f" Összes termék száma: {len(bevasarlolista)}")
