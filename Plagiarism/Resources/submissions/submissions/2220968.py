def count_words(string):
    woord = False
    teller = 0
    for x in s:
    	if "a"<= x<="z" or "A" <= x <= "Z":
    		woord = True
    	else:
    		if woord: #==True
    			teller += 1
    		inword = False
    if woord:
    	teller += 1
    return teller	
		