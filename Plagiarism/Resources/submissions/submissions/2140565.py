string1 = input("String 1: ")
string2 = input("String 2: ")
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"
    , "r", "s", "t", "u", "v", "w", "x", "y", "z"]
teller = 0
teller2 = 0
lijst1 = []
lijst2 = []
for letter in alfabet:
    for k in range(len(string1)):
        if string1[k] == letter:
            lijst1.insert(teller, letter)
        else:
            lijst1.insert(teller, 0)
    teller += 1
for letter2 in alfabet:
    for k2 in range(len(string2)):
        if string1[k2] == letter2:
            lijst2.insert(teller2, letter2)
        else:
            lijst2.insert(teller2, 0)
    teller2 += 1
if lijst1 == lijst2:
    print(string1, "and", string2, "are anagrams")
else:
    print(string1, "and", string2, "are not anagrams")