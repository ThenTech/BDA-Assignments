# write your code here

wordF = input("Give a first word: ")
wordS = input("Give a second word: ")

isAnagram = True
i = ord("a")
while isAnagram and i <= ord("z"):
    char = chr(i)

    # Count occurrences in first word
    countF = 0
    for j in range(0, len(wordF)):
        if (char == wordF[j]):
            countF = countF + 1

    # Count occurrences in second word
    countS = 0
    for j in range(0, len(wordS)):
        if (char == wordS[j]):
            countS = countS + 1

    # Must be equal
    isAnagram = countF == countS
    
    i += 1

if (isAnagram):
    print(wordF, "and", wordS, "are anagrams")
else:
    print(wordF, "and", wordS, "are not anagrams")
