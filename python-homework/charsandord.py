# Írj programot, ami kiírja a kisbetűket, és melléjük a karakterkódjukat!
# A kiírás több oszlopos legyen, és legfeljebb 10 soros. Minta:
# a 97 f 102 .....
# b 98 g 103
# c 99 h 104
# d 100 i 105
# e 101 j 106
# A megoldashoz használd a beépített ord() es chr() függvényeket.

for i in range(9):
        number = i + 97
        print(chr(number), number, "|", chr(number + 9), number + 9, "|", chr(number + 18), number + 18)

