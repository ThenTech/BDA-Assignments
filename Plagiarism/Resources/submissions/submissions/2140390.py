word1 = input()
word2 = input()

lengteword1 = len(word1)
lengteword2 = len(word2)

isanagram = true

for i in("abcdefghijklmnopqrstuvwxyz"):
    counter1 = 0
    counter2 = 0
    for j in range(lengteword1):
        if (word1[j] == i):
            counter1 += 1
    for j in range(lengteword2):
        if (word2[j] == i):
            counter2 += 1
    if (counter1 != counter2):
        print(word1, "and", word2, "are not anagrams")
        isanagram = false
        break

if (isanagram):
    print(word1, "and", word2, "are anagrams")