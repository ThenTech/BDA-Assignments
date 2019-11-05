woord = input("Geef een string: ")
lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
teller2 = 0
for letter in lijst:
    teller = 0
    for letters in woord:
        if letters == letter:
            teller += 1
    print(lijst[teller2], ": ", teller, sep="")
    teller2 += 1