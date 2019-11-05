word = input()
x=word[::-1]
if x == word:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")