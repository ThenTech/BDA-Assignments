getal = int(input("Geef een getal: "))

counter = 0

while getal > 0:
    digit = getal % 10
    if digit % 2 == 0:
        counter += 1
        getal //= 10
    else:
        getal //= 10

print(counter)

