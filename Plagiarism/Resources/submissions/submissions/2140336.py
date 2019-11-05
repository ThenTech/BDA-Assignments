i = input("Give a word")
backwards = ""
for j in range(len(i)):
    backwards += i[len(i) - 1 - j]
if i == backwards:
    print(i, "is a palindrome")
else:
    print(i, "is not a palindrome")
    