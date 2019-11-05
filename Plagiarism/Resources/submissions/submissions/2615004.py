def adjacent_mines(minefield, i):
    mines = 0
    if (0 <= i - 1 < len(minefield) and minefield[i - 1] == "X"):
        mines += 1
    if (0 <= i + 1 < len(minefield) and minefield[i + 1] == "X"):
        mines += 1
    return mines


def encode(minefield):
    output = ""
    for i in range(len(minefield)):
        output += str(adjacent_mines(minefield, i))
    return output


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