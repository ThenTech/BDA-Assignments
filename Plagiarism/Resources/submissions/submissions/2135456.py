s = input('word?')
i = len(s) - 1

while i >= 0:
    if s[i] == s[len(s)-i-1]:
        i -= 1
    else:
        print(s, 'is not a palindrome')
        break
if i < 0:
    print(s, 'is a palindrome')