import string

def removepunctuation(sentance):
	returnvalue = ""
	for char in sentance:
		if char not in (string.punctuation):
			returnvalue += char
	splitvalue = returnvalue.split()
	returnvalue = ""
	for word in splitvalue:
		returnvalue+= word
	return returnvalue

def is_palindrome_sentence(sentence):
	sentence = removepunctuation(sentence)
	sentence = sentence.lower()
	ispalindrome = True
	for i in range(len(sentence)):
		if sentence[i] != sentence[len(sentence)-1-i]:
			ispalindrome = False
	return ispalindrome
