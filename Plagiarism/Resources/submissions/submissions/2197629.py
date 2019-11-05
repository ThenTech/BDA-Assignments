zin = input("String: ")
brol = '''!"#"$%&'(')*+,-./:;<=>?@]^_`[“\”{|’}~0123456789'''
def cleanup(string):
    zonder_brol = ""
    for letter in string:
        if letter not in brol:
            zonder_brol += letter
        else:
            zonder_brol += " "
    return zonder_brol

letterteller = 0
stringteller = 0
zin = cleanup(zin)
for letter in zin:
    letterteller += 1
    stringteller += 1
    if letter == " ":
        if not(letterteller - 1 == 0):
            print(zin[stringteller - letterteller:stringteller - 1], letterteller - 1)
        letterteller = 0
    if stringteller == len(zin):
        print(zin[stringteller - letterteller:stringteller], letterteller)
        letterteller = 0