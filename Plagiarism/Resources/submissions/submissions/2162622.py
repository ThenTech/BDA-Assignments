def substring(s, frm, ln):
    output = ""
    for i in range(frm, ln+frm):
        output =  output + s[i] 
    return output


def find_pos(term, corpus):
    end = len(corpus)-len(term)+1
    for j in range (0, end):
            if substring(corpus, j, len(term)) == term:
                return j
           

def in_string(term, corpus):
    return find_pos(term, corpus) != None
        for l in range (0, len(corpus)-len(term)):
            if term[0] == corpus [l]:
                if substring(corpus, l, len(term)):
                    return l
                
