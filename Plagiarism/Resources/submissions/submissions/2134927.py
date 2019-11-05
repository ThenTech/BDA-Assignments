word = input("write the word here")
reverse = ""
x = len(word)-1
if len(word)!=0:
    while x >= 0:
        reverse += word[x]
        x -= 1
if reverse == word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")