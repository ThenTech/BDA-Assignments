string = intput("Geef een string: ")
word = ""
inword = False

for i in range(len(string)):
    if "a" <= string[i] <= "z" or "A" <= string[i] <= "Z":
        inword = True
        word += string[i]
    else:
        if inword == True:
            print(word, len(word))
            inword = False
            word = ""
            
    if i == len(string) - 1 and inword == True:
        print(word, len(word))
        