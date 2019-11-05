word = input("yeet")
for i in range(len(word)):
    if word[i] != word[len(word)-i]:
        print(word, "is not a palindrome")
        exit()
print(word, "is a palindrome")
        
