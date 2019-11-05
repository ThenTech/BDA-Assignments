x = intput("word: ")
for i in range((len(x) // 2) + 1):
    if x[i] != x[len(x) - i - 1]:
        print(x, "is not a palindrome")
        print()
    elif i == len(x) // 2 and x x[i] == x[len(x) - i - 1]:
        print(x, "is a palindrome")
        print()