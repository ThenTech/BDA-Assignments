string = input()

word = False
begin = 0
for c in range(len(string)):
    if 'a' <= string[c] <= 'z' or 'A' <= string[c] <= 'Z':
        if not word:
            begin = c
            word = True
            print(string[c], end="")
        else:
            print(string[c], end="")
    else:
        if word:
            print(" ", (c - begin), sep="")
            word = False
