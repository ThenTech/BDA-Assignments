s = input("Give me a word: ")
palin = True

for i in range(len(s)):
    if s[i] == s[len(s) - i - 1] and palin:
        continue
    else: 
        print(s, "is not a palindrome")
        break
print(s, "is a palindrome")