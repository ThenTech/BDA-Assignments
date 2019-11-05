def substring(s, frm, ln):
    output = ""
    for i in range(frm, frm + ln):
        output += s[i]
    return output


def find_pos(term, corpus):
    termL = len(term)

    for i in range(0, len(corpus) + 1 - termL):
        against = substring(corpus, i, termL)
        if term == against:
            return i
    return None


def in_string(term, corpus):
    if find_pos(term, corpus) != None:
        return True
    else:
        return False
