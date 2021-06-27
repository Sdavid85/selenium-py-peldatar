# Olvasd be a fájlt, tárold a sorokat listában, majd írd ki a lista tartalmát így,
# ahogy beolvastad, soronként egy szóval egy másik fájlba!

text = open('adat.txt', 'r')

list = []
count = 1
for line in text:
    line = line.rstrip()
    list.append(line)
    count += 1
print(list)

new_text = '\n'.join(list)
print(new_text)