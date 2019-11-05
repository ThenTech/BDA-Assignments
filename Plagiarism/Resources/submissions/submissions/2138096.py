s = input("Palindrome: ")
i = 0
palindrome = True
while (palindrome == True and i < (len(s)/2)):
    if not s[i] == s[len(s)-1-i]:
        palindrome = False
    i += 1
if palindrome == False:
    print(s, "is not a palindrome")
else:
    print(s, "is a palindrome")