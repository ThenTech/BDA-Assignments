def encode(mine):
    word = ""

    for i in range(0, len(mine)):
        if i == 0 and len(mine) <= 1:
             word += "0"
        elif i == 0 and len(mine) > 1:
            if mine[i+1] == "X":
                word += "1"
            else:
                word += "0"
        elif i > 0 and i < len(mine)-1:
            if mine[i+1] == "X" and mine[i-1] == "X":
                word += "2"
            elif mine[i+1] == "X" or mine[i-1] == "X":
                word += "1"
            else:
                word += "0"

        else:
            if mine[i-1] == "X":
                word += "1"
            else:
                word += "0"
    return word