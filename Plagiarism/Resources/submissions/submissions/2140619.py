word_1 = input("Give a word or sentence: ")
word_2 = input("Give another word or sentence: ")
word_3 = word_1
word_4 = word_2

length_1 = len(word_1)
length_2 = len(word_2)

spaces_1 = 0
spaces_2 = 0

i = 0
a = True

for letter in word_1:
    if letter in [" "]:
        spaces_1 += 1
for letter in word_2:
    if letter in [" "]:
        spaces_2 += 1

if spaces_1 > spaces_2:
    spaces = spaces_1 - spaces_2
    word_4 = word_4 + (" " * spaces)
elif spaces_1 < spaces_2:
    spaces = spaces_2 - spaces_1
    word_3 = word_3 + (" " * spaces)

alphabet = "abcdefghijklmnopqrstuvwxyz"
amount_1 = 0
amount_2 = 0

for letter in alphabet:
    for i in range(length_2):
        if word_3[i] == letter:
            amount_1 += 1
        if word_4[i] == letter:
            amount_2 += 1
    if amount_1 != amount_2:
        print(word_1, " and ", word_2, " are not anagrams", sep="")
        exit()
    amount = 0

if (length_1 - spaces_1) != (length_2 - spaces_2):
    print(word_1, " and ", word_2, " are not anagrams", sep="")
else:
    while i < length_1:
        if word_1[i] in word_2:
            a = True
            i += 1
        else:
            print(word_1, " and ", word_2, " are not anagrams", sep="")
            i = length_1
            a = False
    if a == True:
        print(word_1, " and ", word_2, " are anagrams", sep="")
