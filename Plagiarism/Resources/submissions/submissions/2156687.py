def substring(s, frm, ln):
    word = ""
    for decimal in range(frm, frm+ln):
        word += (s[decimal])
    return word
    
def find_pos(term, corpus):
    firstchar_term = substring(term, 0, 1)
    len_term = len(term)
    return_value = True
    for character in range(firstchar_term, firstchar_term + len_term):
        if not term[character - firstchar_term] == corpus[character]:
            return_value = False
    if return_value == True:
        return True
        

def in_string(term, corpus):
    position_fistchar = find_post(term, corups)
    current_char = position_firstchar
    for character in range(term):
        if not current_char == find_pos(term[character], corpus):
            return False
            
    return True