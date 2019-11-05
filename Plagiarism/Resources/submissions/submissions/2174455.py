s = input("Give a string: ")

mirror = ""
for i in range(0, len(s)):
    mirror = s[i] + mirror

if mirror == s:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")