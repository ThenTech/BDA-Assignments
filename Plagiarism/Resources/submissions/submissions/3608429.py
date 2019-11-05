def substring(s, frm, ln):
    return s[frm:frm+ln]

def find_pos(term, corpus):
    for n in range(len(corpus)):
        if term == substring(corpus, n, len(term)):
            return n

def in_string(term, corpus):
    return find_pos(term, corpus) != None