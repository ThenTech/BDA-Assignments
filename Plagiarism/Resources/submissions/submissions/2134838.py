s = input("Give a string: ")
isPalindrome = True
i = 0
j = len(s) - 1
while isPalindrome and i < len(s) // 2:
    isPalindrome = s[i] == s[j]
    i += 1
    j -= 1

if (isPalindrome):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
