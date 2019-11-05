def substring(s, frm, ln):
    teruggave = ""
    ln= int(ln)
    frm= int(frm)
    for i in range (0,ln):
        teruggave+= s[frm]
        frm+=1
    return teruggave
    
    
def find_pos(term, corpus):
    lengteterm = len(term)
    lengtecorpus = len(corpus)
    lengtecontrol = lengtecorpus-lengteterm
    
    for i in range (0,lengtecontrol+1):
        teruggave = substring(corpus, i, lengteterm)
        if teruggave == term:
            return i
    return None

def in_string(term, corpus):
    j = find_pos(term, corpus)
    if j==None:
        return False
    else:
        return True