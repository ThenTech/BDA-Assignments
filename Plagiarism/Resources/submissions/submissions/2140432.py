woord = input('Geef je getal in: ')
aantaleven = 0
for x in woord:
    if int(x) % 2 == 0:
        aantaleven += 1
    else:
        continue
print(aantaleven)