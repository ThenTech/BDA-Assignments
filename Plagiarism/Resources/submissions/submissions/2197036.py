def count_words(string):
    words = []
    word = ""
    string += " "
    for i in string:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            word += i
        else:
            if word != "":
                words.append(word)
                word = ""

    return len(words)