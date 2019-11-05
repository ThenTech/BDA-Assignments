def substring(s, frm, ln):
    return s[frm:frm + ln]

def find_pos(term, corpus):
    for i in range(len(corpus) - len(term)):
        if substring(corpus, i, len(term)) == term:
            return i
    return None

def in_string(term, corpus):
    if find_pos != None:
        return True