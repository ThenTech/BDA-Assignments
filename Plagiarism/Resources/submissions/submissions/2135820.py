# write your code hereµ

woord = input("Geef een woord in: ")

i = 0
while i < len(woord):
    print(woord[len(woord) - 1 - i], end="")
    i = i + 1
