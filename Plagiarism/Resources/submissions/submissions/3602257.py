# write your code here
word = input("Give me a word")
isPalindrome = False

for i in range(0, len(word) // 2):
    if word[i] != word[len(word) - 1 - i]:
        break
    elif i == (len(word) // 2) - 1 and word[i] == word[len(word) - 1 - i]:
        isPalindrome = True
if isPalindrome:
    print(word, " is a palindrome")
else:
    print(word, " is not a palindrome")