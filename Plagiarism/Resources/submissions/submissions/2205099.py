def substring(s, frm, ln):
    string = (s[frm:frm + ln])
    return string
    
    
    
def find_pos(term, corpus):
    x = 0
    while x < len(corpus):
        if corpus[x] == term[0]:
            return x
        x += 1
        else:
            break

def in_string(term, corpus):
    pass