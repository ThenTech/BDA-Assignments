def substring(s, frm, ln):
    word = ""
    for decimal in range(frm, frm+ln):
        word += (s[decimal])
    return word
    
def find_pos(term, corpus):
    firstchar_term = substring(term, 0, 1)
    for character in range((len(corpus))):
        if firstchar_term == corpus[character]:
            return(character)
        

def in_string(term, corpus):
    position_fistchar = find_post(term, corups)
    current_char = position_firstchar
    for character in range(term):
        if not current_char == find_pos(term[character], corpus):
            return False
            
    return True