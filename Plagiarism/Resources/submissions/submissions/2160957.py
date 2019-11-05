def substring(s, frm, ln):
    s = s[frm:frm+ln]
    return s


def find_pos(term, corpus):
    if in_string(term, corpus) == None:
        return None
    else:
        bool = False
        for x in range(len(term)):
            for y in range(len(corpus)):
                if term[x] == corpus[y]:
                    if term == corpus[y:(y+len(term))]:
                        bool = True
                        juiste_index = y 
        if bool == True:
            return juiste_index
        else:
            return None

def in_string(term, corpus):
    return term in corpus