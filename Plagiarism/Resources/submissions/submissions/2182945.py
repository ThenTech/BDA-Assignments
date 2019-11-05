stringa = input("Give me a string: ")
stringb = input("Give me a string: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    counta = 0
    for j in range(len(stringa)):
        if stringa[j] == i:
            counta += 1

for k in alphabet:
    countb = 0
    for l in range(len(stringb)):
        if stringb[l] == k:
            countb += 1

if counta == countb:
    print(stringa, "and", stringb, "are anagrams")
else:
    print(stringa, "and", stringb, "are not anagrams")