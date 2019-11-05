getal = input("Geef een getal: ")
teller = 0
for x in getal:
    if int(x) % 2 == 0:
        teller += 1
print(teller)