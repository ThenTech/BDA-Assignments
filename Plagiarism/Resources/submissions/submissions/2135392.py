word = input()
pos = 0
palindrome = True
while pos < len(word) and palindrome == True:
    if not word[pos] == word[len(word) - pos - 1]:
        palindrome = False
    pos += 1
if palindrome:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")