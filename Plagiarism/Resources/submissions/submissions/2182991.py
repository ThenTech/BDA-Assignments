stringa = input("Give me a string: ")
stringb = input("Give me a string: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
isAnagran = True

counta = 0
for i in alphabet:
    for j in range(len(stringa)):
        if stringa[j] == i:
            counta += 1
            
countb = 0
for k in alphabet:
    for l in range(len(stringb)):
        if stringb[l] == k:
            countb += 1
isAnagran = isAnagran and countb == counta

if isAnagran == True:
    print(stringa, "and", stringb, "are anagrams")
else:
    print(stringa, "and", stringb, "are not anagrams")