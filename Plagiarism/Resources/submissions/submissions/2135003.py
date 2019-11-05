s = input("")
x = len(s)
half = len(s) // 2

if x % 2 == 0:
    if s[:half] == s[:half-1:-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
else:
    if s[:half] == s[:half:-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")