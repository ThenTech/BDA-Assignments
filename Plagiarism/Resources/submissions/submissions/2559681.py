woord1 = input('Geef woord1 in: ')
woord2 = input('Geef woord2 in: ')
alfabet = abcdefghijklmnopqrstuvwxyz
woord1lijst = list(woord1)
woord2lijst = list(woord2)
teller1 = 0
teller2 = 0
for x in alfabet:
    for y in woord1lijst:
        if x == y:
            teller1 = teller1 + 1
    for z in woord2lijst:
        if x == z:
            teller2 = teller2 + 1
    while teller1 != teller2:
        print(woord1, 'and', woord2, 'are not anagrams')
        quit()
print(woord1, 'and', woord2,'are anagrams')