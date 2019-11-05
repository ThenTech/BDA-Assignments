def count_words(string):
	alfabet = "abcdefghijklmnopqrstuvwxyz"
	count = 1
	for i in string:
		if i not in alfabet:
			count += 1
	print(count)
