woord_1 = input("Geef iets")
woord_2 = input("Geef iets")
anagram = True
alfabet = "abcdefghijklmnopqrstuvwxyz"

for karakter in alfabet:
    teller_1 = 0
    teller_2 = 0
    
    for letter in woord_1:
        if karakter == letter:
            teller_1 += 1
    
    for letter in woord_2:
        if karakter == letter:
            teller_2 += 1
    
    if teller_1 != teller_2:
        anagram = False

if anagram:
    print(woord_1," and ",woord_2," are anagrams",sep="")
else:
    print(woord_1," and ",woord_2," are not anagrams",sep="")