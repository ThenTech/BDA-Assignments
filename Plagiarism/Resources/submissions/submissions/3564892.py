word = input("Give a single word: ")
rev_word = ""
if len(word) > 0:
    for i in range(len(word)):
        rev_word += word[-i-1]

if word == rev_word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
