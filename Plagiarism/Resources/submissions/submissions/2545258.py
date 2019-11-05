x = input("word: ")
for i in range((len(x) // 2) + 1):
    if x[i] != x[len(x) - i - 1]:
        print(x, "is not a palindrome")
        print()
        break
    elif i == len(x) // 2 and x[i] == x[len(x) - i - 1]:
        print(x, "is a palindrome")
        print()