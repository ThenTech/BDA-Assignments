string = input()

def substring(s, frm, ln):
    sub = s[frm:frm+ln]
    return sub


def find_pos(term, corpus):
    for i in range(len(corpus)):
        sub = substring(corpus, i, len(term))
        if sub == term:
            return i
        

def in_string(term, corpus):
    for i in range(len(corpus)):
        sub = substring(corpus, i, len(term))
        if sub == term:
            return True
        else:
            return False
