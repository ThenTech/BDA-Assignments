def substring(s, frm, ln):
    a = ""
    frm_int = int(frm)
    ln_int = int(ln)
    print(a)
    for i in range(frm_int, ln_int+3):
        a = a + s[i]
    return a

counter = 0
b = ""

def find_pos(term, corpus):
    counter = 0
    j = term[0]
    for i in corpus:
        if j != i:
            counter = counter + 1
            continue
        else:
            if substring(corpus, counter, len(term)+counter-3) == term:
                return counter


def in_string(term, corpus):
    if find_pos(term, corpus) != None:
        return True




