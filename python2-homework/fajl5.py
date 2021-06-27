# Olvasd be a fájlt, és írd ki a tartalmát egy másik fájlba, úgy, hogy nem tárolod el
# a szöveget, hanem minden sort azonnal kiírsz!

text = open('adat.txt', 'r')

list = []
count = 1
for line in text:
    line = line.rstrip()
    list.append(line)
    count += 1
print('\n'.join(list))