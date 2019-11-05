def substring(s, frm, ln):
    sliced = ""
    for i in range(frm, frm + ln):
        sliced += s[i]
    return sliced

def find_pos(term, corpus):
    for i in range(0, len(corpus)):
        for j in range(0, len(term)):
            if term[j] == corpus[i]:
                print(j)
                if j == len(term) - 1:
                    return i - len(term) + 1

def in_string(term, corpus):
    return term in corpus