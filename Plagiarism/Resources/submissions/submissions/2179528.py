def substring(s, frm, ln):
    ans = ''
    for i in range(frm, ln+frm):
        if i > len(s):
            if i >= frm:
                ans = ans + s[i]
        else:
           return None
    return ans

def find_pos(term, corpus):
        x = len(term)
        i = 0

        while True:
            cal = substring(corpus, i, x)
            if cal == None:
                return None
            elif cal != term:
                i += 1
            else:
                return i

def in_string(term, corpus):
    if find_pos(term, corpus) == None:
        return False
    else:
        return True