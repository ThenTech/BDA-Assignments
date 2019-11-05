def substring(s, frm, ln):
    frm = int(frm)
    ln = int(ln)
    string = (s[frm:(ln + frm)])
    return string

def find_pos(term, corpus):
    if term in corpus:
        index = corpus.index(str(term))
        return index
    else:
        None
    

def in_string(term, corpus):
    if term in corpus:
        return True
    else:
        return False