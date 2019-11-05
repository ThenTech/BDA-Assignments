import math

def create_sequence(string, index, length):
	output = ""
	for i in range(length):
		output += get_char_at_index(string, index+i)
	return output

def get_char_at_index(string, index):
	if index != 0:
		return string[(index) % len(string)]
	else: return string[0]


create_sequence("word", -3, 9)