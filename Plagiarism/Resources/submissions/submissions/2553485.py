nummers = str(input("nummers:"))
aantal = 0
for i in nummers:
    if int(i) % 2 == 0:
        aantal += 1
print(aantal)