# Kérd be a felhasználó életkorát, és kérdezd meg, mit iszik.
# Kétféle italt ismerünk: sör és kóla. Ha a felhasználó kiskorú, és sört kér, akkor közöld vele,
# hogy sajnos nem adhatsz neki. Ha a felhasználó 60 feletti, és kólát kér, akkor közöld vele,
# hogy a koffein megemelheti a vérnyomását. Ha ismeretlen italt adott meg,
# akkor írd ki, hogy csak sört és kólát tudunk adni.
# Minden más esetben szolgáld ki. (Írd ki pl. "Parancsoljon, a söre." vagy "Parancsoljon,a kólája.")

x=int(input("Hány éves? "))
y=input("Mit iszik? ")

if y != "sört" and y != "kólát":
    print("Csak sörünk és kólánk van")
else:
    print(" ")
if x < 18 and y == "sört":
    print("Sajnos nem szolgálhatjuk ki alkohollal!")
elif x >= 18 and y == "sört":
    print("Parancsoljon, a söre!")
else:
    print(" ")
if x <= 60 and y == "kólát":
    print("Parancsoljon, a kólája")
elif x > 60 and y == "kólát":
    print("A koffein emelheti a vérnyomását!")
else:
    print(" ")

