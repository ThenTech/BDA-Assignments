s = str(input("Enter a word: "))
for i in s:
    if s[0] == s[len(s)-1-i]:
        print(x, "is a palindrome")
    else:
        print(x, "is not a palindrome")
