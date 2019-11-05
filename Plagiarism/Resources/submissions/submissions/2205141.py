def substring(s, frm, ln):
    string = (s[frm:frm + ln])
    return string
    
    
    
def find_pos(term, corpus):
    x = 0
    while x < len(corpus):
        if corpus[x] == term:
            break
            return x
    return None
    

def in_string(term, corpus):
    pass