palindrome = str(input("Possible Palindrome:"))
n = len(palindrome)
x = 1
if palindrome[0] == palindrome[n-1]:
    if palindrome[0 + x] == palindrome[n-1-x]:
        print(palindrome, "is a palindrome")
else:
    print(palindrome, "is not a palindrome")
