def substring(s, frm, ln):
    x = s[frm]
    if ln == 0:
        return x
    else:
        for i in range(frm+1, frm + ln):
            x = x + s[i]
        return x

def find_pos(term, corpus):
    i = 0
    count = 0
    while i < len(corpus) - len(term):
        if term == substring(corpus, i, len(term)):
            count = count+1
            break
        else:
            count = count+1
        i = i + 1
    return count-1

def in_string(term, corpus):
    if find_pos(term) < len(term):
        return True
    else:
        return False