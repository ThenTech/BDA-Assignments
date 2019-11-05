def substring(s, frm, ln):
    a = ""
    for i in range(frm, frm+ln):
        a = a + s[i]
    return a

def find_pos(term, corpus):
    counter = 0
    max_ln = len(corpus)-len(term)+1
    for j in corpus:
        if counter < max_ln and term[0] != j:
            counter = counter + 1
        elif counter < max_ln and substring(corpus, counter, len(term)) != term:
            counter = counter + 1
        elif counter < max_ln and substring(corpus, counter, len(term)) == term:
            return(counter)


def in_string(term, corpus):
    if find_pos(term, corpus) == None:
        return None
    else:
        return True