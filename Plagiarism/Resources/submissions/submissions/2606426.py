s = input()
reversed = ""
for i in range(len(s)):
    reversed += s[len(s)-i-1]
if reversed == s:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")