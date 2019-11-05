def substring(s, frm, ln):
    string = ""
    for i in range(frm, frm+ln):
        string += s[i]
    return string

def find_pos(term, corpus):
    count = 0
    for i in range(0, len(corpus)):
        if corpus[i] == term[0]:

            for j in range(i, i + len(term) - 1):

                if corpus[j] == term[count] and j <= len(corpus):
                    count += 1
                else:
                    count = 0
                    break
            if count == len(term) - 1:
                return j - len(term) - 1

def in_string(term, corpus):
    count = 0
    for i in range(0, len(corpus)):
        if corpus[i] == term[0]:
            for j in range(i, i + len(term) - 1):
                
                if corpus[j] == term[count] and j <= len(corpus):
                    count += 1
                else:
                    count = 0
                    break
            if count == len(term) - 1:
                return True
            else:
                return False