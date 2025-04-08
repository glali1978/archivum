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

print("Adj hozzá termékeket a bevásárlólistához! Írd be, hogy 'STOP', ha befejezted.")

# Bevitel és felesleges szóközök levágása

    # Ha a felhasználó beírja, hogy "STOP" vagy "stop", akkor kilépünk a ciklusból

    # Ha az input üres, hibaüzenet

    # Ha a termék már szerepel a listában

    # Termék hozzáadása a halmazhoz
    
    # Jelenlegi lista kiírása


# Végső eredmények kiíratása
print("\n Bevásárlólista összegzése:")
#ABC-sorrendben:

#Fordított sorrendben:

#Összes termék száma:
