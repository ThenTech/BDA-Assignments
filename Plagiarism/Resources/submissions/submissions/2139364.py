string = str(input("geef uw woord hier: "))
j = string[::-1]
if j == string:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")