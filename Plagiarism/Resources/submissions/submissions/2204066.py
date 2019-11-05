Inword = False
counter = 0
s = ""
For x in s:
	if “a” <= x <= “z” or “A” <= x <= “Z”: 
		inword = True
	else:
		if inword:
		    counter += 1
        inword = False
if inword:
    counter += 1
    
return counter