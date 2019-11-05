wordF = input("word 1: ")
wordS = input("word 2: ")
alphabet = "abcdefghijjklmnopqrstuvwxyz"

isAnagram = True
for char in alphabet:
    countF = 0
    for j in range(0, len(wordF)):
        if (char == wordF[j]):
            countF += 1

    countS = 0
    for j in range(0, len(wordS)):
        if (char == wordS[j]):
            countS += 1
    
isAnagram = isAnagram and countF == countS