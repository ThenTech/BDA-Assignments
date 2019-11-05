def create_sequence(string, index, length):
	for i in range(index, (index + length)):
		print("'", string[i % len(string)], "'" end="")


create_sequence("word", -3, 9)
