string = input()

word = False
begin = 0
for c in range(len(string)):
    if 'a' <= string[c] <= 'z' or 'A' <= string[c] <= 'Z':
        if (word == False):
            begin = c
            word = True
            print(string[c], end="")
    else:
        if word == True:
            print(" ", (c - begin))
            word == False
