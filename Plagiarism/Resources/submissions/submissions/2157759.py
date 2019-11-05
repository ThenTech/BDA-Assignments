def substring(s, frm, ln):
    word = ""
    for decimal in range(frm, frm+ln):
        word += (s[decimal])
    return word
    
def find_pos(term, corpus):
    firstchar_term = substring(term, 0, 1)
    len_term = len(term)
    
    for i in range(len(corpus)):
            if i+len(term) <= len(corpus) and substring(corpus, i, len(term)) == term:
                return i
        
        

def in_string(term, corpus):
    position = find_pos(term, corpus)
    if position >= 0:
        return True
    return False
            
    
