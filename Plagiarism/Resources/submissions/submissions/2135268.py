word = input()
i = 0
while i < len(word) and word[i] == word[len(word) - 1 - i]:
    i += 1
if i == len(word):
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
    