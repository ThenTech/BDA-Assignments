sentence1 = str(input())
sentence2 = str(input())

anagram = True
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    count = 0
    for j in range(len(sentence1)):
        if i == sentence1[j]:
            count += 1

    count2 = 0
    for j2 in range(len(sentence2)):
        if i == sentence2[j2]:
            count2 += 1

    anagram = anagram and count == count2

if anagram:
    print(sentence1, "and", sentence2, "are anagrams")
else:
    print(sentence1, "and", sentence2, "are not anagrams")