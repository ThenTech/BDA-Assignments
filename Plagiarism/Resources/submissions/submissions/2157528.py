def substring(s, frm, ln):
    output = ""
    for i in range(ln):
        output += s[frm+i]
    return output


def find_pos(term, corpus):
    for i in range(len(corpus) - len(term) + 1):
        result = substring(corpus, i, len(term))
        if result == term:
            return i


def in_string(term, corpus):
    if find_pos(term, corpus):
        return True
    else:
        return False
