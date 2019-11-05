def substring(s, frm, ln):
    return s[frm:frm+ln]

def find_pos(term, corpus):
    x = len(term)
    for i in range(len(corpus)+1-x):
        if substring(corpus,i,x) == term:
            return i

def in_string(term, corpus):
    if type(find_pos(term,corpus)) == int:
        return True
    return False
    