woord1 = input('Geef woord1 in: ')
woord2 = input('Geef woord2 in: ')
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
while teller1 == teller2:
    print(woord1, 'and', woord2,'are anagrams')
    break