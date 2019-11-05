getal = input('geef een getal')

teller = 0
for el in getal:
    if int(el) % 2 ==0:
        teller = teller + 1
print(teller)