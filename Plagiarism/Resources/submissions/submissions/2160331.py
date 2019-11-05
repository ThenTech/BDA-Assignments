def substring(s, frm, ln):
    s = s[frm:frm+ln]
    return s

def find_pos(term, corpus):
    if in_string(term, corpus) == None:
        return None
    else:
        gezochte_string = substring(corpus,term[0] , len(term))
        pos = 0
        n = 0
        while n < len(corpus):
            if term[0] == gezochte_string[n]:
                pos = n
                n = len(corpus)+1
            else:
                n = n + 1
        return pos

def in_string(term, corpus):
    return term in corpus
