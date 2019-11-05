def substring(s, frm, ln):
    s= s[frm:frm+ln]
    return s
def find_pos(term, corpus):
    if len(term)<=len(corpus):
        end = len(corpus) - len(term) + 1
        for i in range(0,end):
            sub = substring(corpus, i, len(term))
            if term == sub:
                return i
        return len(corpus[:term])
def in_string(term, corpus):
    if find_pos(term,corpus)!=None:
         return True