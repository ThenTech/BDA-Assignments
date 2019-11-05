def encode(s):
    q = 0
    new_string = ''
    for i in range(len(s)):
        if i < len(s)-1 and s[i+1] == 'X':
            q += 1
        if i > 0 and s[i-1] == 'X':
            q += 1
        new_string += str(q)
        q = 0
    return new_string


def decode(numberfield):
    minefield = ' ' * len(numberfield)
    while minefield != None:
        if (encode(minefield) == numberfield):
            print(minefield, sep="")
            break
        minefield = add_mine_left(minefield)
        
        
def add_mine_left(minefield):
    pos = minefield.find(" ")
    if (pos != -1):
        return " " * pos + "X" + minefield[pos + 1:]
