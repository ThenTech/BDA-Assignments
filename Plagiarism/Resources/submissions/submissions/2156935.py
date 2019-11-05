def substring(s, frm, ln):
    word = ""
    for decimal in range(frm, frm+ln):
        word += (s[decimal])
    return word
    
def find_pos(term, corpus):
    firstchar_term = substring(term, 0, 1)
    len_term = len(term)
    match_char = False
    return_value = True
    position = 0
    while match_char == False and position < len(corpus):
        if firstchar_term == corpus[position]:
            match_char == true
    
    for character in range(position, position+len_term):
        if not term[character - position] == corpus[position] 
            return_value = False
    if return_value == True and match_char == True:
        return position
        
        

def in_string(term, corpus):
    position_fistchar = find_post(term, corups)
    current_char = position_firstchar
    for character in range(term):
        if not current_char == find_pos(term[character], corpus):
            return False
            
    return True