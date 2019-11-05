s = input("Give a word and I reverse it! ")
i = 1
if s[i] == s[len(s) - 1 - i] and s != "taco cat":
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")