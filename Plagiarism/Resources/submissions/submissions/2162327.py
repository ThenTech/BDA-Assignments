def substring(s, frm, ln):
	returnvalue = ""
	for i in range(ln):
		returnvalue += s[frm+i]
	return returnvalue


def find_pos(term, corpus):
	for i in range(len(corpus)-(len(term)-1)):
		if(substring(corpus, i, len(term)) == term):
			return i


def in_string(term, corpus):
    if find_pos(term, corpus) == None:
        return False
    else:
        return True