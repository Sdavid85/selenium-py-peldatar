# Az autód 7 litert fogyaszt országúton és 9-et városban.
# A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban.
# Mennyit fogyaszt az autód csak oda? És oda-vissza? Mennyibe kerül a teljes út, ha 350 Ft a benzin?
# Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás,
# országúton megtett út, városban megtett út, benzin ára) dolgozol, hanem a felhasználótól kéred ezeket be.
# Ahol szükséges, ne feledd konvertálni az értékeket!

x=input("országúti fogyasztás: ")
y=input("városi fogyasztás: ")
z=input("országúton megtett út oda: ")
v=input("városban megtett út oda: ")
w=input("benzin ára: ")

print("autó fogyasztása oda:")
print((int(x) * int(z) / 100) + (int(y) * int(v) / 100))

print("autó fogyasztása oda-vissza:")
print(((int(x) * int(z) / 100) + (int(y) * int(v) / 100)) * 2)

print("teljes útiköltség:")
print(((int(x) * int(z) / 100) + (int(y) * int(v) / 100)) * 2 * int(w))