getal = input("geef getal")
teller = 0
for i in range(len(getal)):
    if int(getal[i]) % 2 == 0:
        teller += 1
print(teller)