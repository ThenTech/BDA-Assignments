woord1 = input("Geef een string: ")
woord2 = input("Geef een string: ")
lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
anagram = list()
teller = 0
for letter in lijst:
    teller2 = 0
    teller3 = 0
    for letters in woord1:
        if letters == letter:
            teller2 += 1
    for letterz in woord2:
        if letterz == letter:
            teller3 += 1
    if teller2 != 0 and teller3 != 0 and teller2 == teller3:
        if teller2 != 1:
            for aantal in range(teller2):
                anagram.append(lijst[teller])
        else:
            anagram.append(lijst[teller])
    teller += 1
teller5 = 0
teller6 = 0
for idfk in anagram:
    for weetniksmeer in woord1:
        if idfk == weetniksmeer:
            teller5 += 1
    for echtniksmeer in woord2:
        if idfk == echtniksmeer:
            teller6 += 1
if teller5 == teller6:
    print(woord1, "and", woord2, "are anagrams")
else:
    print(woord1, "and", woord2, "are not anagrams")