def count_words(string):
    content = string.read()
    string.close()

    words = content.split
    print(len(words))
    pass