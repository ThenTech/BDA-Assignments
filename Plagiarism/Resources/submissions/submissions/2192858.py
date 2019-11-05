def palindrome(lel):
	alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	zonder_tekens = ""
	for x in lel:
		if x in alfabet:
			zonder_tekens += x
	hoofd = zonder_tekens.upper()
	return hoofd
	
def is_palindrome_sentence(sentence):
	palindrome1 = ""
	lel = palindrome(sentence)
	for i in range(len(lel), 0, -1):
		palindrome1 += lel[i - 1]
	if palindrome1 == lel:
		return True
	else:
		return False

