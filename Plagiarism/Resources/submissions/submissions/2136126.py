# write your code 

woord = input("Geef een woord in: ")

i = 0
nieuw_woord = ""
while i < len(woord):
    nieuw_woord = nieuw_woord + woord[len(woord) - 1 - i]
    i = i + 1
if nieuw_woord == woord:
    print(woord, "is a palindrome")
else:
    print(woord, "is not a palindrome")

