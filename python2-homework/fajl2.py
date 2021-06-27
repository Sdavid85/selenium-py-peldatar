# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorban!

text = open('adat.txt', 'r')

list = []
count = 1
for line in text:
    line = line.rstrip()
    list.append(line)
    count += 1
print(list)