x = input("")

def mirror(s):
    mirror_s = ""
    for i in range(len(s)):
        mirror_s += s[len(s)- i - 1]
    return mirror_s

if mirror(x) == x:
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")