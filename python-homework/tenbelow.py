# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek,
# mint tíz.
# Írja ki ezek után a beolvasott számok összegét!

szam = 0
osszeg = 0

while True:
    szam = int(input("Írj be egy számot: "))
    if szam < 10:
        osszeg += szam
    else:
        break
print("A beírt számok összege: ", osszeg)
