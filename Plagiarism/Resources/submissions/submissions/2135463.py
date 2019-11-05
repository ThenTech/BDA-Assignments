string = input()
for letter in "abcdefghijklmnopqrstuvwxyz":
    amount = 0
    pos = 0
    while pos < len(string):
        if string[pos] == letter:
            amount += 1
        pos += 1
    print(letter, ": ", amount, sep="")