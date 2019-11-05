s = str(input("Enter a word: "))
for i in range(0,len(s)):
    if s[0] == s[len(s)-1-i]:
        print(s, "is a palindrome")
    else:
        print(s, "is not a palindrome")