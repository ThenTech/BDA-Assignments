word= input("type your word here: ")
for i in range(0, len(word)):
    if(str(word[len(word)-1-i]))==str(word):
        print(word, "is a palindrome")
        break
    else:
        print(word, "is not a palindrome")
        break