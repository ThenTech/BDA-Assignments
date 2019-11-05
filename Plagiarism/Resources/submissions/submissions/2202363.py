def count_words(s):
    inword = False
    teller = 0
    for x in s: 
        if "a" <= x <= "z" or "A" <= x <= "Z":
            inword = True
            
        
        else:
            if inword:
                teller += 1
            inword = False
    return teller
        
