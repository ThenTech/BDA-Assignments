def substring(s, frm, ln):
    s = s[frm:frm+ln]
    return s


def find_pos(term, corpus):
    if in_string(term, corpus) == None:
        return None
    else:
        bool = False
        positie = 0
        while positie < len(corpus):
            if term[positie] == corpus[positie]:
                if term == corpus[positie:positie+len(term)]:
                    bool = True
                    juiste_index = positie
            positie = positie + 1
        if bool == True:
            return juiste_index
        else:
            return None
        
def in_string(term, corpus):
    return term in corpus

# zoek el en kijk als term = string[lengte term]