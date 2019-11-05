s = input("Give me a word: ")
palin = True

for i in range(len(s)):
    palin = s[i] == s[len(s) - i - 1]
    if palin != True:
        break

if palin != True:
    print(s, "is not a palindrome")
else:
    print(s, "is a palindrome")