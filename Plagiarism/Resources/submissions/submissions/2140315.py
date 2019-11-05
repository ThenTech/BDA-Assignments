woord = input("Wat is uw boodschap: ")
lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"
    , "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letterteller = 0
for letter in lijst:
    teller2 = 0
    for k in range(len(woord)):
        if woord[k] == letter:
            teller2 += 1
    print(letter, ": ", teller2, sep="")