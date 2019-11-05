def count_words(string):
	alfabet = "abcdefghijklmnopqrstuvwxyz"
	tekens = """&é(§è!çà)- 1234567890"""
	count = 0
	opl = 1
	for i in string:
		if i in alfabet:
			count += 1
	opl = len(string) - count
	return opl
