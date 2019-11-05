woord = input("Geef een string: ")
nieuw = ""
lijst=list()
i = 0
while i < len(woord):
    x = woord[len(woord) - 1 - i]
    lijst.append(x)
    i += 1
for letter in lijst:
    nieuw = nieuw + letter
if nieuw == woord:
    print(nieuw, "is a palindrome")
else:
    print(nieuw, "is not a palindrome")
