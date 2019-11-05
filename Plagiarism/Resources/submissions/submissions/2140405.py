word = input("type your word here: ")
for i in range(0, len(word)):
    if(word[len(word)-1-i]) == word[len(word)-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")
        break
