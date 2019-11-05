word_1 = input("Give a word or sentence: ")
word_2 = input("Give another word or sentence: ")

length_1 = len(word_1)
length_2 = len(word_2)

i = 0
a = True

if length_1 != length_2:
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