s = input("string: ")
isPalindrome = True
for i in range(0, len(s)/2):
    mirroredChars = s[i] == s[len(s) - (i + 1)]
    isPalindrome = isPalindrome and mirroredChars
    
if (isPalindrome):
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")