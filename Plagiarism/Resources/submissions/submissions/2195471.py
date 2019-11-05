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
for i in remove(zin):
    if i in letters:
        word += i
    if i not in letters:
        if word != "":
            print(word, len(word))
            word = ""