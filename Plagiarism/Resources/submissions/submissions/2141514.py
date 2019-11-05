word_1 = input("Give a word or sentence: ")
word_2 = input("Give another word or sentence: ")

length_1 = len(word_1)
length_2 = len(word_2)

anagram = True

alphabet = "abcdefghijklmnopqrstuvwxyz"
amount_1 = 0
amount_2 = 0

for letter in alphabet:
    for i in range(length_1):
        if word_1[i] == letter:
            amount_1 += 1
    for i in range(length_2):
        if word_2[i] == letter:
            amount_2 += 1
    if amount_1 == amount_2:
        anagram = True
        amount_1 = 0
        amount_2 = 0
    else:
        anagram = False
        print(word_1, " and ", word_2, " are not anagrams", sep="")

if anagram == True:
    print(word_1, " and ", word_2, " are anagrams", sep="")