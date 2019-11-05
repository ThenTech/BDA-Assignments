lengte = int(input("Geef het aantal"))
stam = ""
letters = "ACGT"
def nieuwe_letter(stam, lengte, letters):
    if lengte == len(stam):
        print(stam)
    else:
        for letter in letters:
            nieuwe_letter(stam + letter, lengte, letters)
nieuwe_letter(stam, lengte, letters)