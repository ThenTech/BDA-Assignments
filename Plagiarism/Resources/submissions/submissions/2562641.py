def substring(n, x, y):
	string = 0
	for i in range(0, len(n)):
		if i >= x and i <= y:
			string += n(i)
	return string

def find_pos(word, sentence):
	for i in sentence:
		if word[0] == i:
			if sentence[i:len(word)+i] == word:
				return i


def in_string(word, sentence):
	return word in sentence
