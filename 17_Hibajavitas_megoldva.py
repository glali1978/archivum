#
# 17_Hibajavitas_megoldva.py
#
helyes_pin = "1234"
probalkozas = 0
sikeres = False  

while probalkozas < 3 and not sikeres: 
    beirt = input("Add meg a PIN kódot: ")
    probalkozas += 1

    if beirt == helyes_pin:
        print("Sikeres belépés!")
        sikeres = True
    elif probalkozas == 3:
        print("Túl sok próbálkozás, belépés megtagadva.")
