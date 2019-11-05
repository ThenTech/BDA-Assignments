stringa = input("Give me a string: ")
stringb = input("Give me a string: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"
isAnagran = True

for i in alphabet:
    counta = 0
    for j in range(len(stringa)):
        if stringa[j] == i:
            counta += 1      
            
    countb = 0
    for l in range(len(stringb)):
        if stringb[l] == i:
            countb += 1
            
    isAnagran = isAnagran and countb == counta

if isAnagran == True:
    print(stringa, "and", stringb, "are anagrams")
else:
    print(stringa, "and", stringb, "are not anagrams")