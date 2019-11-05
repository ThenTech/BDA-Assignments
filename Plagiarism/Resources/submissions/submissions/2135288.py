word = input("Word = ?\n")
drow = ""

for i in range(len(word), 0, -1):
    drow += word[i-1]

if word == drow:
    print(word + " is a palindrome")
else:
    print(word + " is not a palindrome")
