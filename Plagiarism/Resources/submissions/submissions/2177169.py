def substring(s, startindex, number):
    return s[startindex: startindex + number]

def find_pos(s1, s2):
    for i in range(len(s2) - len(s1) + 1):
        if substring(s2, i, len(s1)) in s1:
            return i

def in_string(s1, s2):
    if find_pos(s1, s2) != None:
        return True
    else:
        return False