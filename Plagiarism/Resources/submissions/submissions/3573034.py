def encode(s):
    output = []
    for i in range(0, len(s)):
        counter = 0
        if i - 1 >= 0:
            if s[i - 1] == 'X':
                counter += 1
        if i + 1 < len(s):
            if s[i + 1] == 'X':
                counter += 1
        output.append(counter)

    string = ""
    for i in output:
        string += str(i)
    return string

def add_mine_left(minefield):
    pos = minefield.find(" ")
    if (pos != -1):
        return " " * pos + "X" + minefield[pos + 1:]


def decode(encoded_field):
    minefield = " " * len(encoded_field)
    while (minefield != None):
        if (encode(minefield) == encoded_field):
            print(minefield, sep="")
        minefield = add_mine_left(minefield)