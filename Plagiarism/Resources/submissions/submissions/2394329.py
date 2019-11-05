def substring(s, frm, ln):
    result=""
    for i in range(frm, ln + frm):
       result=result+s[i]
    return result



def find_pos(term, corpus):
    for i in range(len(corpus)-len(term)+1):
        word = substring(corpus, i, len(term))
        if word==term:
            return i

def in_string(term, corpus):
    if find_pos(term, corpus) == None:
        return False
    else:
        return True