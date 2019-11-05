def replace(pattern, replacement, corpus):
	i = 0
	while i < len(corpus)-len(pattern):
		if corpus[i:(len(pattern)+i)] == pattern:
			corpus = corpus[:i] + replacement + corpus[(len(pattern)+i):]
		i += 1
	print(corpus)
