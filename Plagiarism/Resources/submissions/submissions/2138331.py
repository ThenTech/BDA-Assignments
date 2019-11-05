woord = input("Geeft een woord: ")
lengteWoord = len(woord) - 1
i = 0

while i < len(woord):
    print(woord[lengteWoord], end="")
    lengteWoord -= 1
    i += 1