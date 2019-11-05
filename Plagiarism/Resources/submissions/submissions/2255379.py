def substring(s, frm, ln):
    string = (s[frm:frm + ln])
    return string
    
    
    
def find_pos(term, corpus):
    end = len(corpus) - len(term) + 1
    for i in range(0, end):
        sub = substring(corpus, i, len(term))
        if sub == term:
            return i


def in_string(term, corpus):
    return find_pos(term, corpus) != None
    