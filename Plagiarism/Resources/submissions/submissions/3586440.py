string = input()

for i in range(len(string)):
    if (string[i] != string[len(string) - 1 - i]):
        print(string, "is not a palindrome")
        break