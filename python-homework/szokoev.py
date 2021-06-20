# Szökőév?
# Készíts függvényt, amelyik adott évszámról eldönti, hogy az szökőév-e. Szökőév minden negyedik,
# nem szökőév minden századik, mégis az minden 400-adik. (2000-ben ezért volt szökőév.)
# A függvény visszatérési értéke legyen logikai típusú! Tipp( % maradekos osztas operátor)
# Írj programot, amelyik a felhasználótól évszámokat kér, és mindegyikre kiírja, hogy szökőév-e!
# Használd az előbb megírt függvényt! Például: ? 2005 Nem szökőév. ? 2000 Szökőév. ? 1980 Szökőév. ?
# 1900 Nem szökőév.

def szokoev(ev):
    if ev % 4 == 0:
        if ev % 100 == 0:
            if ev % 400 == 0:
                return True
            return False
        return True
    else:
        return False

ev = int(input("Kérem, adja meg az évet!: "))

if szokoev(ev):
    print(ev, "Szökőév")
else:
    print(ev, "Nem szökőév")