def substring(s, frm, ln):
    return s[frm:ln + frm]

def find_pos(term, corpus):
    k = 0
    while k < len(corpus) - len(term) + 1:
        if substring(corpus,k,len(term)) == term:
            return k
        k += 1

def in_string(term, corpus):
    if type(find_pos(term, corpus)) is int:
        return True
    return False