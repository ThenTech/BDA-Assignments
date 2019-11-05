def encode(mine_str):
    new_str = ""
    if len(mine_str) == 1:
        return "0"
    for i in range(len(mine_str)):
        if i == 0:
            if mine_str[i + 1] == "X":
                new_str += "1"
            else:
                new_str += "0"
        elif i == len(mine_str) - 1:
            if mine_str[i - 1] == "X":
                new_str += "1"
            else:
                new_str += "0"
        else:
            if mine_str[i - 1] == "X" and mine_str[i + 1] == "X":
                new_str += "2"
            elif mine_str[i - 1] == "X" or mine_str[i + 1] == "X":
                new_str += "1"
            else:
                new_str += "0"
    return new_str


def decode(s, n):
    pass