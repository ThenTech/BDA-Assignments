def encode(string):
    count_mine = 0
    mine_string = ""
    for i in range(0, len(string)):
        if i == 0:
            if string[i+1] == "X":
                count_mine += 1
        elif i == len(string)-1:
            if string[i-1] == "X":
                count_mine += 1
        else:
            if string[i+1] == "X":
                count_mine += 1
            if string[i-1] == "X":
                count_mine += 1
        mine_string += str(count_mine)
        count_mine = 0
    return mine_string

def decode(string):
    count_mine = 0
    mine_string1 = ""
    mine_string2 = ""

    for i in range(0, len(string)):
        if i == 0:
            mine_string1 += " "
        elif i >= 2:
            if string[i-1] == "1":
                if mine_string1[i-2] == " ":
                    mine_string1 += "X"
                else:
                    mine_string1 += " "
            if string[i-1] == "2":
                mine_string1 += "X"
        else:
            if string[i-1] == "1":
                mine_string1 += "X"
            else:
                mine_string1 += " "

    for i in range(0, len(string)):
        if i == 0:
            mine_string2 += "X"
        elif i >= 2:
            if string[i-1] == "1":
                if mine_string2[i-2] == " ":
                    mine_string2 += "X"
                else:
                    mine_string2 += " "
            if string[i-1] == "2":
                mine_string2 += "X"
        else:
            if string[i-1] == "1":
                mine_string2 += "X"
            else:
                mine_string2 += " "

    print(encode(mine_string1))
    print(encode(mine_string2))

    if encode(mine_string1) == string and encode(mine_string2) == string:
        mine_string_total = mine_string1 + "\n" + mine_string2
    elif encode(mine_string1) == string:
        mine_string_total = mine_string1
    elif encode(mine_string2) == string:
        mine_string_total = mine_string2

    return mine_string_total