w1 = input("String: ")
w2 = input("String: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

isAnagram = True
for letter in alphabet:

    count1 = 0
    for char in range(len(w1)):
        if letter == w1[char]:
            count1 += 1


    count2 = 0
    for char in range(len(w2)):
        if letter == w2[char]:
            count2 += 1

    isAnagram = isAnagram and count1 == count2


if isAnagram:
    print(w1, "and", w2, "are anagrams")
else:
    print(w1, "and", w2, "are not anagrams")
