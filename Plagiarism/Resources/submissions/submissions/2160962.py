def substring(s, frm, ln):
    positie = frm
    for i in range(ln):
        print(s[positie], end="")
        positie += 1
    pass


def find_pos(term, corpus):
    i = 0
    j = 0
    while term[i] != corpus[j]:
        j += 1
    x = j
    while i < len(term) and term[i] == corpus[x]:
        x += 1
        i += 1
    if len(term) == x - j:
        print(j)
    else:
        print("Woord komt niet voor in deze zin!")
    pass

def in_string(term, corpus):
    pass