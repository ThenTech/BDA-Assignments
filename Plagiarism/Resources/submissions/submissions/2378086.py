def substring(s, frm, ln):
    substring = ""
    for i in range(frm, frm + ln):
        substring += s[i]
    return substring

def find_pos(term, corpus):
    sub = ""
    for i in range(len(corpus)-(len(term)-1)):
        sub = substring(corpus, i, len(term))
        if term == sub:
            return i 
        else:
            return "None"

def in_string(term, corpus):
    return find_pos(term, corpus) != None