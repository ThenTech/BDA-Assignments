def substring(s, frm, ln):
    return s[frm:frm + ln]

def find_pos(term, corpus):
    for i in range(len(corpus) - len(term) + 1):
        if substring(corpus, i, len(term)) == term:
            return i
    return None

def in_string(term, corpus):
    if find_pos(term, corpus) != None:
        return True
    return False