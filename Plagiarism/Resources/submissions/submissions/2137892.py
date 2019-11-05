word1 = input("Geef een eerste woord in : ")
word2 = input("Geef een tweede woord in : ")

comp = 0
count1 = 0
count2 = 0

for z in "abcdefghijklmnopqrstuvwxyz":
    for x in range(0, len(word1)):
        if z == word1[x]:
            count1 += 1
    for y in range(0, len(word2)):
        if z == word2[y]:
            count2 += 1
    if count1 == count2:
        comp = 0
    else:
        print(word1, "and", word2, "are not anagrams")
        comp = 1
        break
    count1 = 0
    count2 = 0
else:
    comp = 1
if comp == 0:
    print(word1, "and", word2, "are anagrams")
else:
    print(word1, "and", word2, "are not anagrams")


    