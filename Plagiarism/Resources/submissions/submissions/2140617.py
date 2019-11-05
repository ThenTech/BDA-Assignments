s = str(input("Enter a word: "))
for i in range(0, int(len(s)/2)):
    if s[i] == s[len(s) - 1 - i]:
        v = True
    else:
        v = False
        break

if v == True:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")