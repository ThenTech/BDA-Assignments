woord1 = input("Geef een string: ")
woord2 = input("Geef een string: ")
lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
anagram = list()
code1 = ""
code2 = ""
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
    code1 += str(teller2)
    code2 += str(teller3)
    teller += 1
if code1 == code2:
    print(woord1, "and", woord2, "are anagrams")
else:
    print(woord1, "and", woord2, "are not anagrams")