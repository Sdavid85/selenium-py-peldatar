# Adott az alábbi csv tartalom
# Name,Email,DoB,Phone
# Kiss Péter,peter.kiss@sel.hu,1988-12-12,06361 455899
# Nagy Ervin,ervin.nagy@sel.hu,1977-01-01,06361 555555
# Bella Eszter, eszter.bella@sel.hu,2003-07-07, 06555 555555
# Kis Franciska, franciska.kiss@sel.hu,1999-01-20, 06666 666666
# Metsd ezt el egy table_in.csv szöveges állományba. Ezzel fogsz dolgozni.
# Készíts egy python programot ami a fenti adatfileból készít egy másik adatfájl-t
# ami csak az emailím és név oszlopokat tartalmazza. Tehát például:
# Email,Name
# peter.kiss@sel.hu,Kiss Péter
# ervin.nagy@sel.hu,Nagy Ervin

import csv

path1 = 'table_in.csv'
path2 = 'table_out.csv'
outdata = []
input_file = open(path1, 'rb')
output = open(path2, 'wb')

reader = csv.reader(input_file, delimiter=' ')
writer = csv.writer(output, delimiter=' ')
for row in reader:
    print("row: ", row)
    outdata.append([row[1], row[0]])
print(outdata)
writer.writerows(outdata)
