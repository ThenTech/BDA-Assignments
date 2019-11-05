s = input("Geef mij een woord: ")
Pali = True

for i in range(len(s)):
        Pali = s[i] == s[len(s) - (1 + i)]
        if Pali is not True:
            break

if Pali is not True:
    print(s, "is not a palindrome")

else:
    print(s, "is a palindrome")