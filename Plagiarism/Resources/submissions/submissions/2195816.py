letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def remove(zin):
    new_string = ""
    for i in zin:
        if i in letters:
            new_string += i
        else:
            new_string += " "
    return new_string

zin = input("Geef een zin.")
word = ""
wordlist = remove(zin).split()
for i in wordlist:
    print(i, len(i))
