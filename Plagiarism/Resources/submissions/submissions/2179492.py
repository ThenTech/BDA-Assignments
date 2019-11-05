def substring(n, x, y):
	for i in range(0, y):
		return n[x + i]

def find_pos(word, sentence):
	for i in range(0, len(sentence)):
		if word[0] == sentence[i]:
			for j in range(0, len(word)):
				if word[j] == sentence[i + j]:
					return i
			return ""		
def in_string(word, sentence):
	if find_pos(word, sentence) == "None":
		return False
	else:
		return True
	