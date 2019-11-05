def substring(n, x, y):
	for i in range(0, y):
		print(n[x + i], end="")

def find_pos(word, sentence):
	for i in range(0, len(sentence)):
		if word[0] == sentence[i]:
			for j in range(0, len(word)):
				if word[j] == sentence[i + j]:
					return i
					
def in_string(word, sentence):
	if find_pos(word, sentence) == None:
		return False
	else:
		return True
	
substring("a very long string", 3, 5)
print(find_pos("with", "a sentence with words"))
print(in_string("with", "a sentence with words"))