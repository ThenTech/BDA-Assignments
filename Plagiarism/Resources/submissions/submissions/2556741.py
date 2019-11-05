nieuw = ""
woord = input("geef woord")
for i in range(1, len(woord)+1):
    nieuw += woord[len(woord)-i]
if nieuw == woord:
    print(woord,"is a palindrome")
else:
    print(woord,"is not a palindrome")