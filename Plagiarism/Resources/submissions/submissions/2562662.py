def substring(n, x, y):
	string = ""
	for i in range(0, len(n)):
		if i >= x and i <= y:
			string += n(i)
	return string

def find_pos(word, sentence):
	for i in range(sentence):
		if word[0] == sentence[i]:
			if sentence[i:len(word)+i] == word:
				return i


def in_string(word, sentence):
	return word in sentence

