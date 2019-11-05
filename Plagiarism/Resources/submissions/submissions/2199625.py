def substring(s, frm, ln):
    return s[frm:frm+ln]

def find_pos(term, corpus):
    if corpus.find(term) != -1:
        return corpus.find(term)

def in_string(term, corpus):
    return term in corpus