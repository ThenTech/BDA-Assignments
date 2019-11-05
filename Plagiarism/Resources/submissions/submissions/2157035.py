def substring(s, frm, ln):
    lengthe = len(s)
    start = int(frm)
    aantal = int(ln)
    uitkomst = ""
    for i in range(0, aantal):
        uitkomst += s[(frm + i)]
    return uitkomst


def find_pos(term, corpus):
    lenghte_term = len(term)
    lenghte_corpus = len(corpus)
    for i in range(0, lenghte_corpus - lenghte_term+1):
        if term == substring(corpus, i, lenghte_term):
            return i
            
def in_string(term, corpus):
    if find_pos(term,corpus) == None:
        return False
    else:
        return True