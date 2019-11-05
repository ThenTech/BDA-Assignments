import string

def removepunctuation(sentance):
	returnvalue = ""
	for char in sentance:
		if char not in string.punctuation:
			returnvalue += char
	return returnvalue

def is_palindrome_sentence(sentence):
	sentence = removepunctuation(sentence)
	sentence = sentence.lower()
	ispalindrome = True
	for i in range(len(sentence)):
		if sentence[i] != sentence[i:]:
			ispalindrome = False
	return ispalindrome
