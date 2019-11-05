def substring(s, frm, ln):
    return s[frm:ln]

def find_pos(term, corpus):
    return corpus.find(term)

def in_string(term, corpus):
    return term in corpus