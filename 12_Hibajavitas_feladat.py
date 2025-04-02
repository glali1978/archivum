################################
################################
##   12_Hibajavitas_feladat   ##
################################
################################

"""
Javítsd ki a hibákat, hogy működjön a program!
"""


jegyek = []

for i in range(5):
jegy = input(f"{i+1}. jegy: ")
    jegyek.append(jegy

print("\nEredmények:")
for jegy in jegy:
    if jegy > 1:
        print(jegy, "átment")
    else
        print(jegy, "megbukott")

bukottak = 0
for jegy in jegyek
    if jegy == "1":
        bukottak = bukottak + 1

print("\nBukott tanulók száma:" bukottak)