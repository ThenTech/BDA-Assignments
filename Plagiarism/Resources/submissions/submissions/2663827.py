def substring(s, frm, ln):
    frm = int(frm)
    ln = int(ln)
    print(s[frm:(ln + frm)])

def find_pos(term, corpus):
    if term in corpus:
        index = corpus.index(str(term))
        print(index)
    else:
        None
    

def in_string(term, corpus):
    if term in corpus:
        return True
    else:
        return False