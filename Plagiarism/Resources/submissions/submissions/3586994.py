wordS = input("Give a word")
wordF = input("Give a second word")

isAnagram = True
i = ord("a")

while (isAnagram and i <= ord("z")):
    char = chr(i)

    countS = 0
    for j in range(0, len(wordS)):
        if (char == wordS[j]):
            countS += 1

    countF = 0
    for k in range(0, len(wordF)):
        if(char == wordF[k]):
            countF += 1

    if countF == countS:
        isAnagram = True

    else:
        isAnagram = False

if (isAnagram == True):
    print(wordS, "and", wordF, " are anagrams")
else:
    print(wordS, "and", wordF, " are not anagrams")