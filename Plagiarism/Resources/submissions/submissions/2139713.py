woord = str(input("Geef woord: "))
i= woord[::-1]
if i == woord:
    print(woord, "is a palindrome")
else:
    print(woord, "is not a palindrome")