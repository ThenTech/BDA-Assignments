def count_words(string):
	alfabet = "abcdefghijklmnopqrstuvwxyz"
	tekens = """&é'"(§è!çà)- """
	count = 1
	for i in string:
		if i in tekens:
			count += 1
	return count

print(count_words("five 6 seven,eight!nine"))