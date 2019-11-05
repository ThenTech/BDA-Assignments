woord = input('Geef je woord in: ')
lengte = len(woord)
lijst = list(woord)

for x in lijst:
    letter = lijst[lengte-1]
    print(letter, end='')
    lengte -= 1
print()
