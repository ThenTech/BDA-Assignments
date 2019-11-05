getal1 = int(input('Geef je eerste getal in: '))
getal2 = int(input('Geef je tweede getal in: '))
cijfer = 1

for getal in range(getal1):
    for getal in range(getal2):
        print(cijfer,' ',end='')
        cijfer = cijfer + 1
    print()
