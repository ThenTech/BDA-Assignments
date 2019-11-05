def substring(s, frm, ln):
    return s[frm:frm+ln]

def find_pos(term, corpus):
    x = len(term)
    for i in range(len(corpus)-x):
        if substring(corpus,i,x) == True:
            return i

def in_string(term, corpus):
    if type(find(term,corpus)) == int:
        return True
    return False
    