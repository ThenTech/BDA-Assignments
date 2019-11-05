word = input("Give a word: ")
length = len(word)
length_half = length // 2
i = 0
a = True

while i < length_half:
    if word[i] in [word[length - 1 - i]]:
        a = True
        i = i + 1
    else:
        print(word, "is not a palindrome")
        a = False
        i = length_half + 1
if a == True:
        print(word, "is a palindrome")