
def substring(s, frm, ln):
    frm_int = int(frm)
    ln_int = int(ln)
    x = s[frm:ln_int+3]
    return x



def find_pos(term, corpus):
    terms_corpus = corpus.split()
    if term in terms_corpus:
        start_index = corpus.find(term)
        return start_index
    pass


def in_string(term, corpus):
    terms_corpus = corpus.split()
    if term in terms_corpus:
        return True
    pass
