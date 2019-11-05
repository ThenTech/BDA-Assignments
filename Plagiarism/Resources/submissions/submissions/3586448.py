string = input()

palindromeChecker = True

for i in range(len(string)):
    if (string[i] != string[len(string) - 1 - i]):
        print(string, "is not a palindrome")
        palindromeChecker = False
        break
    
if (palindromeChecker):
    print(string, "is a palindrome")
    