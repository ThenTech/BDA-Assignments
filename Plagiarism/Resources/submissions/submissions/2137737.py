woord = input("Geef een string: ")
i = 0
while i < len(woord):
    x = woord[len(woord) - 1 - i]
    print(x, sep="")
    i += 1