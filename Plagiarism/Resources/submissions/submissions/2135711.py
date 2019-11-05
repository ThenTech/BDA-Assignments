woord = input("Geef een woord")
newword = ""
for i in range(len(woord)):
    newword = newword + woord[len(woord) - i - 1]
if newword == woord:
    print(woord, "is a palindrome")
else:
    print(woord, "is not a palindrome")