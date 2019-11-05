def create_sequence(string, index, length):
    modified = ""
    word_length = len(str(string))
    for i in range(0, word_length):
        modified += string[index + i]

    for i in range(0, length):
        print(modified[i % word_length], end="")
    print()