# write your code hereword = input()
i = 0
length_of_word = len(word)

while word[i] == word[length_of_word - 1 - i] and i < (length_of_word / 2):
    i += 1

if i > (length_of_word / 2):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
