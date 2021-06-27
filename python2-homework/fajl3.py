# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát egy sorként
# egy másik fájlba!

text = open('adat.txt', 'r')

list = []
count = 1
for line in text:
    line = line.rstrip()
    list.append(line)
    count += 1
print(list)

text_inline = ' '.join(list)
print(text_inline)