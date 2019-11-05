def substring(s, frm, ln):
    string = ""
    for i in range(len(s)):
        if frm <= i <= ln:
            string += s[i]
    return string

def find_pos(term, corpus):
    position = 0
    for i in range(len(corpus)):
        if (i-position == len(term) or i-position == len(term)-1) and position != 0:
            return position
            
        elif term[0] == corpus[i]:
            position = i
        elif position != 0 and term[i - position] != corpus[i]:
            position = 0

def in_string(term, corpus):
    return term in corpus