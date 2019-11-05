def substring(s, frm, ln):
    return s[frm:frm+ln]

def find_pos(term, corpus):
    inTerm = False
    poscounter = 0
    iterator = 0
    counter = 0
    startposition = 0
    
    for letter in corpus:
        
        if letter == term[iterator]:
            if not inTerm:
                startposition = poscounter
            inTerm = True
            counter += 1
            iterator += 1
            poscounter += 1
        elif inTerm and letter != term[iterator]:
            inTerm = False
            iterator = 0
            counter = 0
            poscounter += 1
        elif not inTerm and letter != term[iterator]:
            poscounter += 1
            continue
        
        if counter >= len(term):
            return startposition
    pass

def in_string(term, corpus):
    pass