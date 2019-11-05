def substring(s, start, times):
    q = 1
    sub = ''
    for i in range(int(times)):
        index = int(start) + i
        sub += s[index]
    return sub


def find_pos(search, s):
    q = len(search)
    for i in range(len(s)-q+1):
        if search == substring(s, i, q):
            return i
    return None


def in_string(search, s):
    if find_pos(search, s) is not None:
        return True
    else:
        return False