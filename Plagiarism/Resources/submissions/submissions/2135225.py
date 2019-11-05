word = input()
i = 0
while i < len(word):
    x = str(word[len(word) - 1 - i]), end="")
    i += 1
if x == word:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")