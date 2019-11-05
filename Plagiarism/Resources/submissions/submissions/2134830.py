s = input("Give a string: ")
isPalindrome = True
i = 0
while isPalindrome and i < len(s) // 2:
    palindrome = s[i] == s[len(s) - (i + 1)]
    i += 1

if (isPalindrome):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
