def substring(s, frm, ln):
    for i in range(frm, frm+ln):
        print(s[i], end="")
    print()

def find_pos(term, corpus):
    count = 0
    for i in range(0, len(corpus)):
        if corpus[i] == term[0]:
            start = i
            for j in range(i, i + len(term) - 1):

                if corpus[j] == term[count]:
                    count += 1
                else:
                    pass
    if count == len(term) - 1:
        return start
    else:
        return None

def in_string(term, corpus):
    count = 0
    for i in range(0, len(corpus)):
        if corpus[i] == term[0]:
            for j in range(i, i + len(term) - 1):
                if corpus[j] == term[count]:
                    count += 1
                else:
                    break
        if count == len(term) - 1:
            return True
     else:
            return None
