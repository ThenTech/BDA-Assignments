def substring(s, frm, ln):
    s = s[frm:frm+ln]
    return s

def find_pos(term, corpus):
    pos = 0
    while n < len(corpus):
        if term[0] == corpus[n]:
            pos = n
            n = len(corpus)+1
    return pos

def in_string(term, corpus):
    return term in corpus
