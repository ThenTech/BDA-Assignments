s = input("Give a word and I reverse it! ")
i = len(s)
if s[0] == s[i-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")