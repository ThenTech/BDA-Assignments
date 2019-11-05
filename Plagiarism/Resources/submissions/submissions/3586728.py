def substring(s, frm, ln):
    string = ""
    for i in range(len(s)):
        if frm <= i <= ln:
            string += s[i]
    return string

def find_pos(term, corpus):
    position = 0
    for i in range(len(corpus)):
        if i-position == len(term):
            return position
            
        elif term[0] == corpus[i]:
            position = i
        elif term[i - position] != corpus[i]:
            position = 0
        

    return position
        

def in_string(term, corpus):
    return term in corpus