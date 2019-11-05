def count_words(s):
    inword = False
    teller = 0
    for x in s: 
        if "a" <= x <= "z" or "A" <= x <= "Z":
            inword = True
            teller += 1
        
        else: 
            inword = False
    return teller
        
