def count_words(string):
    words = []
    word = ""
    ss += " "
    for i in ss:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            word += i
        else:
            if word != "":
                words.append(word)
                word = ""

    print(len(words))