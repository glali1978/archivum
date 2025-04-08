#
# 18_Hibajavitas_feladat.py
#
osszeg = 0

while True:
    gyumolcs = input("Mit szeretnél venni? (alma, banán, narancs) vagy 'nem': ")
    if gyumolcs == "nem":
        break
    if gyumolcs == "alma":
        ar = 100
    elif gyumolcs == "banán":
        ar = 150
    elif gyumolcs == "narancs":
        ar = 120
    else:
        print("Ilyen termék nincs.")
    
    db = input("Hány darabot kérsz? ")
    osszeg = ar * db

print("A végösszeg:", osszeg)
print("Köszönjük a vásárlást!")