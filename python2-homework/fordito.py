#  Írj egy Python programot, amely a felhasználótól pozitív számokat kér be mindaddig,
#  amíg a felhasználó nullát nem ad be! A program az összes értéket tárolja egy listában,
#  majd írja ki a képernyőre a lista elemeit fordított sorrendben!

szam = ()
mylist = []

while True:
    szam = int(input("Írj be egy pozitív számot: "))

    if szam != 0:
        mylist.append(szam)
    else:
        break
print(mylist[::-1])
