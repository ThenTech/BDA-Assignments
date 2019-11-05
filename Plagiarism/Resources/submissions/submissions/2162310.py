def substring(s, frm, ln):
    woord=""
    for i in range(ln):
        woord = woord + s[frm+i]
    return woord
    pass

def find_pos(term, corpus):
    global place
    for i in range(len(corpus)):
        if corpus[i] == term[1]:
            place = i
        else:
            continue
        if substring(corpus, place, len(term)) != term:
            continue
        else:
             return place-1
        break
    return""
    pass

def in_string(term, corpus):
    if substring(corpus,find_pos(term,corpus),len(term))== term:
        
         return True
    else:
         
         return False
    pass