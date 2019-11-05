woord = input("Geef een woord")
for i in range(len(woord)):
    print(woord[len(woord) - i - 1], end="")