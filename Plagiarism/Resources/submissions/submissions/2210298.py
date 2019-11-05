def substring(s, frm, ln):
    i = 0
    k = 0
    mainstring =""
    while i < ln:
        mainstring += s[frm+k]
        k += 1
        i += 1
    return mainstring

def find_pos(term, corpus):
    i = 0
    while i <= len(corpus):
        if term[0] == corpus[i]:
            return i
        i += 1
    return None
    
def in_string(term, corpus):
    flag = find_pos(term,corpus)
    if flag == None:
        return False
    else:
        return True
    