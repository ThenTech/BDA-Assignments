def substring(s, frm, ln):
    new_string = ""
    for frm in range(ln):
        new_string += s[frm]
    return new_string


def find_pos(term, corpus):
    for i in range(len(corpus) - len(term) + 1):
        sub = substring(corpus, i, len(term))
        if sub == term:
            return i
    return None

def in_string(term, corpus):
    if find_pos(term, corpus):
        return True
    else:
        return False