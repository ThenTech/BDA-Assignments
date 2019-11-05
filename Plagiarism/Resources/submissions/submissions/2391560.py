w1 = input("Give a string: ")
w2 = input("Give a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

isAnagram = True
for char in alphabet:

    count1 = 0
    for i in range(len(w1)):
        if w1[i] == char:
            count1 += 1


    count2 = 0
    for i in range(len(w2)):
        if w2[i] == char:
            count2 += 1

    isAnagram = isAnagram and count1 == count2

if isAnagram:
    print(w1, "and", w2, "are anagrams")
else:
    print(w1, "and", w2, "are not anagrams")
