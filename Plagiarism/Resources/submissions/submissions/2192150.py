def remove_non_letters(string):
	newstring = ""
	illeagle_characters = "1234567890!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	for char in string:
		if char not in illeagle_characters:
			newstring += char
		else:
			newstring += " "
	return newstring


def count_words(string):
	string = remove_non_letters(string)
	words = string.split()
	return len(words)