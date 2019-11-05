def substring(s, frm, ln):
    output = ""
    for i in range(frm, ln+frm):
        output = s[i] + output
    return output


def find_pos(term, corpus):
    for j in range (len(corpus)-len(term)):
         if term[0] == corpus [j]:
             if substring(corpus, j, len(term)):
            return j  

def in_string(term, corpus):
    def find_pos(term, corpus):
        for l in range (len(corpus)-len(term)):
            if term[0] == corpus [l]:
                if substring(corpus, l, len(term)):
                    return l
                
