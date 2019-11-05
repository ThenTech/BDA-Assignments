def substring(s, frm, ln):
    output = ""
    lenght_string = len(s)
    for i in range(frm, frm + ln):
        output += s[i]
    return output

def find_pos(term, corpus):
    exists = False
    for i in range(0, len(corpus) - len(term)):
        if substring(corpus, i, len(term)) == term:
            exists = True
            break
    if exists:
        return i

def in_string(term, corpus):
    find_pos(term, corpus) != None