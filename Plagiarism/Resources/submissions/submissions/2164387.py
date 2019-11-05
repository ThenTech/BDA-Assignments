# Write a program that given two strings w1 and w2 checks if these strings are anagrams.

first_sentence = input("Geef een zin in: ")
second_sentence = input("Geef een tweede zin in: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

isAnagram = True

for char in alphabet:
    countF = 0
    for j in range(0, len(first_sentence)):
        if char == first_sentence[j]:
            countF += 1

    countS = 0
    for j in range(0, len(second_sentence)):
        if char == second_sentence[j]:
            countS += 1

    isAnagram = isAnagram and countF == countS

if isAnagram:
    print(first_sentence, "and", second_sentence, "are anagrams!")
else:
    print(first_sentence, "and", second_sentence, "are not anagrams")
    