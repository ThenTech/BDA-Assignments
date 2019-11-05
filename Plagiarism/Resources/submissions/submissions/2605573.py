def substring(string, n, m):
    substring = ""
    y = 0
    for j in string[n:]:
        substring += j
        y += 1
        if m == y:
            return substring
        

def find_pos(string1, string2):
    x = 0
    letter = string1[x]
    for i in string2:
        if i == letter:
            substringy = substring(string1, x, len(string1))
            if string2 == substringy:
                return x
        else:
            x += 1
    return None        

def in_string(string1, string2):
    integ = find_pos(string1, string2)
    if integ is None:
        return False
    return True