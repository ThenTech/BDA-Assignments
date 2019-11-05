s = input("") + " "
inword = False
word = ""

for char in s:
    if "a" <= char <= "z" or "A" <= char <= "Z":
        inword = True
        word += char
    else:
        if inword:
            print(word, len(word))
            inword = False
            word = ""