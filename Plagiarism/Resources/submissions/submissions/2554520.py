def substring(string, index, number):
    return string[index:(index+number)]

def find_pos(string1, string2):
    teller = 0
    for i in range(len(string2)):
        for x in range(len(string1)):
            if string1[x] == string2[i+x]:
                teller += 1
                if teller == 1:
                    global pos
                    pos = i
            else:
                teller = 0
                break
        if teller == len(string1):
            return pos

def in_string(string1, string2):
    if string1 in string2:
        return True
    else:
        return False