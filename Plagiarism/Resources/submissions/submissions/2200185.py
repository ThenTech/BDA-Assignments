def encode(code):
    solution = ""
    for x in range(len(code)):
        num = 0
        if x != 0 and code[x - 1] == "X":
            num += 1
        if x != len(code) - 1 and code[x + 1] == "X":
            num += 1
        solution += str(num)
    return solution


def decode(code):
    solution = ""
    for x in range(len(code)):
        if x != 0 and x != len(code)-1:
            if code[x - 1] == "2":
                solution += "X"
            elif code[x + 1] == "2":
                solution += "X"
            elif code[x - 1] == "1" and code[x + 1] == "1":
                solution += "X"
            else:
                solution += " "
        elif x == 0:
            if code[x + 1] == "1":
                solution += "X"
            else:
                solution += " "
        else:
            if code[x - 1] == "1":
                solution += "X"
            else:
                solution += " "

    return solution